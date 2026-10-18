# sub_008BB987

- RVA: `0x008BB987`–`0x008BB9AC` (길이 `37` bytes)
- VA: `0x00000001408BB987`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082E78`
- 디코드: `11`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008BB98B` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x008BB99C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008BB99C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008BB987  48 8D 4D 48                     lea rcx, [rbp + 0x48]
008BB98B  E8 80 FD FA FF                  call 0x14086b710
008BB990  8B C3                           mov eax, ebx
008BB992  48 8B 8D A0 00 00 00            mov rcx, qword ptr [rbp + 0xa0]
008BB999  48 33 CC                        xor rcx, rsp
008BB99C  E8 9F 0C DF FF                  call 0x1406ac640
008BB9A1  48 81 C4 D8 01 00 00            add rsp, 0x1d8
008BB9A8  5B                              pop rbx
008BB9A9  5D                              pop rbp
008BB9AA  C3                              ret
008BB9AB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008BB987(void)
{
    __int64 result;
    __int64 v_rsp;

    result = SeReleaseSubjectContext(v_rbp + 72, a2, a3, a4);
    a1 = (*(unsigned __int64 *)(v_rbp + 160)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (472);
    return result;
}
```

## 5. (Beta) C Style

```c
void sub_008BB987(void)
{
    int64_t result;
    int64_t local_rsp;

    result = SeReleaseSubjectContext(local_rbp + 72, a2, a3, a4);
    a1 = (*(uint64_t *)(local_rbp + 0xA0)) ^ (local_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (472);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008BB987&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008BB987[BB_008BB987]
  bb_008BB9AB[BB_008BB9AB]
```
