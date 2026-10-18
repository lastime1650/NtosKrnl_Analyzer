# HalpFlushAndWait

- RVA: `0x006ACC30`–`0x006ACC58` (길이 `40` bytes)
- VA: `0x00000001406ACC30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFDA8`
- 디코드: `12`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006ACC39` → [HalpAcpiFlushCache](../48/HalpAcpiFlushCache_function_00484CD0.md) (function, `0x00484CD0`)

### Direct callers
- [HaliCompleteAcpiAPSleep](../56/HaliCompleteAcpiAPSleep_function_0056B320.md) at `0x0056B3CF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006ACC30  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
006ACC35  48 83 EC 28                     sub rsp, 0x28
006ACC39  E8 92 80 DD FF                  call 0x140484cd0
006ACC3E  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
006ACC43  F0 FF 01                        lock inc dword ptr [rcx]
006ACC46  F3 90                           pause
006ACC48  83 39 00                        cmp dword ptr [rcx], 0
006ACC4B  75 F9                           jne 0x1406acc46
006ACC4D  0F 20 D0                        mov rax, cr2
006ACC50  0F 22 D0                        mov cr2, rax
006ACC53  48 83 C4 28                     add rsp, 0x28
006ACC57  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpFlushAndWait(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (40);
    result = HalpAcpiFlushCache(a1, a2, a3, a4);
loc_006ACC46:
    if ((*(unsigned int *)(v_stack_p8)) != 0) goto loc_006ACC46;
    v_rsp = (v_rsp) + (40);
    return v_cr2;
}
```

## 5. (Beta) C Style

```c
int64_t HalpFlushAndWait(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (40);
    result = HalpAcpiFlushCache(Arg1, a2, a3, a4);
loc_006ACC46:
    if ((*(uint32_t *)(v_stack_p8)) != 0) goto loc_006ACC46;
    local_rsp = (local_rsp) + (40);
    return v_cr2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006ACC30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006ACC30[BB_006ACC30]
  bb_006ACC46[BB_006ACC46]
  bb_006ACC4D[BB_006ACC4D]
  bb_006ACC30 -->|flow| bb_006ACC46
  bb_006ACC46 -->|branch| bb_006ACC46
  bb_006ACC46 -->|fallthrough| bb_006ACC4D
```
