# sub_009A64EA

- RVA: `0x009A64EA`–`0x009A6520` (길이 `54` bytes)
- VA: `0x00000001409A64EA`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009C7C4`
- 디코드: `15`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009A64FB` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009A64FB` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009A64EA  49 8D 4E 60                     lea rcx, [r14 + 0x60]
009A64EE  48 89 0F                        mov qword ptr [rdi], rcx
009A64F1  48 8B 8D F0 04 00 00            mov rcx, qword ptr [rbp + 0x4f0]
009A64F8  48 33 CC                        xor rcx, rsp
009A64FB  E8 40 61 D0 FF                  call 0x1406ac640
009A6500  48 81 C4 18 06 00 00            add rsp, 0x618
009A6507  41 5E                           pop r14
009A6509  41 5D                           pop r13
009A650B  5F                              pop rdi
009A650C  5D                              pop rbp
009A650D  C3                              ret
009A650E  CC                              int3
009A650F  48 C7 07 00 00 00 00            mov qword ptr [rdi], 0
009A6516  EB D9                           jmp 0x1409a64f1
009A6518  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009A64EA(void)
{
    __int64 result;
    __int64 v_rsp;

    *(unsigned __int64 *)(v_rdi) = v_r14 + 96;
loc_009A64F1:
    a1 = (*(unsigned __int64 *)(v_rbp + 1264)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (0x618ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
void sub_009A64EA(void)
{
    int64_t result;
    int64_t local_rsp;

    *(uint64_t *)(local_rdi) = local_r14 + 96;
loc_009A64F1:
    a1 = (*(uint64_t *)(local_rbp + 0x4F0)) ^ (local_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (0x618ULL);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A64EA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A64EA[BB_009A64EA]
  bb_009A64F1[BB_009A64F1]
  bb_009A650E[BB_009A650E]
  bb_009A6518[BB_009A6518]
  bb_009A64EA -->|flow| bb_009A64F1
  bb_009A650E -->|branch| bb_009A64F1
```
