# MiLocateSubsectionNode

- RVA: `0x002BBEE0`–`0x002BBF3C` (길이 `92` bytes)
- VA: `0x00000001402BBEE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006DFD0`
- 디코드: `21`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiRemoveMappedPtes](../29/MiRemoveMappedPtes_function_00296A50.md) at `0x00296C27`
- [MiAdvanceVadView](../2A/MiAdvanceVadView_function_002A60EC.md) at `0x002A6183`
- [sub_002BBA31](Unknown_function_002BBA31.md) at `0x002BBA5D`
- [sub_002BBA31](Unknown_function_002BBA31.md) at `0x002BBAA8`
- [sub_0032EA98](../32/Unknown_function_0032EA98.md) at `0x0032EB60`
- [MiDereferenceDataSubsections](../69/MiDereferenceDataSubsections_function_00692530.md) at `0x00692587`
- [sub_006E720A](../6E/Unknown_function_006E720A.md) at `0x006E7281`
- [sub_00884EE1](../../page/88/Unknown_function_00884EE1.md) at `0x00884F4F`
- [sub_0088535F](../../page/88/Unknown_function_0088535F.md) at `0x008854A2`
- [MiPfPrepareReadList](../../page/93/MiPfPrepareReadList_function_0093CD5C.md) at `0x0093D4A5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002BBF36` → [sub_002BC05D + 0x1](Unknown_function_002BC05D.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002BBEE0  4C 8B DC                        mov r11, rsp
002BBEE3  53                              push rbx
002BBEE4  41 56                           push r14
002BBEE6  48 81 EC C8 00 00 00            sub rsp, 0xc8
002BBEED  0F 57 C0                        xorps xmm0, xmm0
002BBEF0  33 C0                           xor eax, eax
002BBEF2  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
002BBEF7  48 8B DA                        mov rbx, rdx
002BBEFA  4C 8B F1                        mov r14, rcx
002BBEFD  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
002BBF02  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
002BBF07  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
002BBF0C  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
002BBF11  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
002BBF16  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
002BBF1A  48 B8 00 00 00 00 00 00 40 00   movabs rax, 0x40000000000000
002BBF24  41 0F 11 43 A8                  movups xmmword ptr [r11 - 0x58], xmm0
002BBF29  41 0F 11 43 B8                  movups xmmword ptr [r11 - 0x48], xmm0
002BBF2E  41 0F 11 43 C8                  movups xmmword ptr [r11 - 0x38], xmm0
002BBF33  48 3B D0                        cmp rdx, rax
002BBF36  0F 83 22 01 00 00               jae 0x1402bc05e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLocateSubsectionNode(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;

    v_rsp = (v_rsp) - (200);
    result = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
}
```

## 5. (Beta) C Style

```c
int64_t MiLocateSubsectionNode(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;

    local_rsp = (local_rsp) - (200);
    result = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x48) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002BBEE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002BBEE0[BB_002BBEE0]
```
