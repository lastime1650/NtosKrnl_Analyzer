# MiReleasePrefetchGapPages

- RVA: `0x00367C08`–`0x00367C2F` (길이 `39` bytes)
- VA: `0x0000000140367C08`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006AD84`
- 디코드: `14`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00367C11` → [MiUnlinkPageChainHead](MiUnlinkPageChainHead_function_00365C40.md) (function, `0x00365C40`)
- `0x00367C25` → [MiReturnPfnReferenceCountAtDpc](MiReturnPfnReferenceCountAtDpc_function_00364010.md) (function, `0x00364010`)

### Direct callers
- [sub_006E313A](../6E/Unknown_function_006E313A.md) at `0x006E33A4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00367C08  40 53                           push rbx
00367C0A  48 83 EC 20                     sub rsp, 0x20
00367C0E  48 8B D9                        mov rbx, rcx
00367C11  E8 2A E0 FF FF                  call 0x140365c40
00367C16  48 85 C0                        test rax, rax
00367C19  75 07                           jne 0x140367c22
00367C1B  48 83 C4 20                     add rsp, 0x20
00367C1F  5B                              pop rbx
00367C20  C3                              ret
00367C21  CC                              int3
00367C22  48 8B C8                        mov rcx, rax
00367C25  E8 E6 C3 FF FF                  call 0x140364010
00367C2A  48 8B CB                        mov rcx, rbx
00367C2D  EB E2                           jmp 0x140367c11
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReleasePrefetchGapPages(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
loc_00367C11:
    result = MiUnlinkPageChainHead(a1, a2, a3, a4);
    if (result != 0) goto loc_00367C22;
    v_rsp = (v_rsp) + (32);
    return result;
loc_00367C22:
    result = MiReturnPfnReferenceCountAtDpc(result, a2, a3, a4);
    goto loc_00367C11;
}
```

## 5. (Beta) C Style

```c
int64_t MiReleasePrefetchGapPages(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
loc_00367C11:
    result = MiUnlinkPageChainHead(Arg1, a2, a3, a4);
    if (result != 0) goto loc_00367C22;
    local_rsp = (local_rsp) + (32);
    return result;
loc_00367C22:
    result = MiReturnPfnReferenceCountAtDpc(result, a2, a3, a4);
    goto loc_00367C11;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00367C08&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00367C08[BB_00367C08]
  bb_00367C11[BB_00367C11]
  bb_00367C1B[BB_00367C1B]
  bb_00367C21[BB_00367C21]
  bb_00367C22[BB_00367C22]
  bb_00367C08 -->|flow| bb_00367C11
  bb_00367C11 -->|branch| bb_00367C22
  bb_00367C11 -->|fallthrough| bb_00367C1B
  bb_00367C21 -->|flow| bb_00367C22
  bb_00367C22 -->|branch| bb_00367C11
```
