# MiFreePlaceholderStorage

- RVA: `0x00AAC868`–`0x00AAC89B` (길이 `51` bytes)
- VA: `0x0000000140AAC868`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060A68`
- 디코드: `17`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AAC873` → [MiGetVadWakeList](../../text/43/MiGetVadWakeList_function_00431134.md) (function, `0x00431134`)
- `0x00AAC88A` → [MiFreePlaceholderVadEvent](../9B/MiFreePlaceholderVadEvent_function_009BB2B4.md) (function, `0x009BB2B4`)
- `0x00AAC894` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiDeleteNewlyCreatedPartialVads](../81/MiDeleteNewlyCreatedPartialVads_function_00810374.md) at `0x00810446`
- [MiDeletePartialCloneVads](../81/MiDeletePartialCloneVads_function_008116E4.md) at `0x00811863`
- [sub_008859DF](../88/Unknown_function_008859DF.md) at `0x00885AA1`
- [sub_00B2A0A2](../B2/Unknown_function_00B2A0A2.md) at `0x00B2A121`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00AAC873` → [MiGetVadWakeList](../../text/43/MiGetVadWakeList_function_00431134.md) (`PAGE` → `.text`)
  - `0x00AAC894` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AAC868  40 53                           push rbx
00AAC86A  48 83 EC 20                     sub rsp, 0x20
00AAC86E  BA 80 00 00 00                  mov edx, 0x80
00AAC873  E8 BC 48 98 FF                  call 0x140431134
00AAC878  48 8B D8                        mov rbx, rax
00AAC87B  48 85 C0                        test rax, rax
00AAC87E  75 07                           jne 0x140aac887
00AAC880  48 83 C4 20                     add rsp, 0x20
00AAC884  5B                              pop rbx
00AAC885  C3                              ret
00AAC886  CC                              int3
00AAC887  48 8B CB                        mov rcx, rbx
00AAC88A  E8 25 EA F0 FF                  call 0x1409bb2b4
00AAC88F  33 D2                           xor edx, edx
00AAC891  48 8B CB                        mov rcx, rbx
00AAC894  E8 D7 5F 0D 00                  call 0x140b82870
00AAC899  EB E5                           jmp 0x140aac880
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFreePlaceholderStorage(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = MiGetVadWakeList(a1, 128, a3, a4);
    if (result != 0) goto loc_00AAC887;
loc_00AAC880:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00AAC887:
    result = MiFreePlaceholderVadEvent(result, 128, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    goto loc_00AAC880;
}
```

## 5. (Beta) C Style

```c
void MiFreePlaceholderStorage(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = MiGetVadWakeList(a1, 128, a3, a4);
    if (result != 0) goto loc_00AAC887;
loc_00AAC880:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00AAC887:
    result = MiFreePlaceholderVadEvent(result, 128, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    goto loc_00AAC880;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AAC868&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AAC868[BB_00AAC868]
  bb_00AAC880[BB_00AAC880]
  bb_00AAC886[BB_00AAC886]
  bb_00AAC887[BB_00AAC887]
  bb_00AAC868 -->|branch| bb_00AAC887
  bb_00AAC868 -->|fallthrough| bb_00AAC880
  bb_00AAC886 -->|flow| bb_00AAC887
  bb_00AAC887 -->|branch| bb_00AAC880
```
