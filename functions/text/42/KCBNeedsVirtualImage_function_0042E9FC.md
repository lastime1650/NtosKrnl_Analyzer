# KCBNeedsVirtualImage

- RVA: `0x0042E9FC`–`0x0042EA2A` (길이 `46` bytes)
- VA: `0x000000014042E9FC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00094EEC`
- 디코드: `13`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0042EA00` → [KCBIsVirtualizable](KCBIsVirtualizable_function_0042EA30.md) (function, `0x0042EA30`)
- `0x0042EA1E` → [CmpIsSystemEntity](../../page/8B/CmpIsSystemEntity_function_008B4E90.md) (function, `0x008B4E90`)

### Direct callers
- [CmKeyBodyReplicateToVirtual](../../page/84/CmKeyBodyReplicateToVirtual_function_00843FE4.md) at `0x00844101`
- [CmpVEExecuteCreateLogic](../../page/A2/CmpVEExecuteCreateLogic_function_00A26F28.md) at `0x00A26F94`
- [CmKeyBodyRemapToVirtual](../../page/AC/CmKeyBodyRemapToVirtual_function_00AC9494.md) at `0x00AC957C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0042EA1E` → [CmpIsSystemEntity](../../page/8B/CmpIsSystemEntity_function_008B4E90.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0042E9FC  48 83 EC 28                     sub rsp, 0x28
0042EA00  E8 2B 00 00 00                  call 0x14042ea30
0042EA05  84 C0                           test al, al
0042EA07  75 06                           jne 0x14042ea0f
0042EA09  48 83 C4 28                     add rsp, 0x28
0042EA0D  C3                              ret
0042EA0E  CC                              int3
0042EA0F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0042EA18  8A 89 32 02 00 00               mov cl, byte ptr [rcx + 0x232]
0042EA1E  E8 6D 64 48 00                  call 0x1408b4e90
0042EA23  84 C0                           test al, al
0042EA25  0F 94 C0                        sete al
0042EA28  EB DF                           jmp 0x14042ea09
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KCBNeedsVirtualImage(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = KCBIsVirtualizable(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0042EA0F;
loc_0042EA09:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0042EA0F:
    result = CmpIsSystemEntity(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a2, a3, a4);
    result = ((unsigned __int8)(result) == 0) ? 1 : 0;
    goto loc_0042EA09;
}
```

## 5. (Beta) C Style

```c
void KCBNeedsVirtualImage(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = KCBIsVirtualizable(a1, a2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_0042EA0F;
loc_0042EA09:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0042EA0F:
    result = CmpIsSystemEntity(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), a2, a3, a4);
    result = ((uint8_t)(result) == 0) ? 1 : 0;
    goto loc_0042EA09;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0042E9FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0042E9FC[BB_0042E9FC]
  bb_0042EA09[BB_0042EA09]
  bb_0042EA0E[BB_0042EA0E]
  bb_0042EA0F[BB_0042EA0F]
  bb_0042E9FC -->|branch| bb_0042EA0F
  bb_0042E9FC -->|fallthrough| bb_0042EA09
  bb_0042EA0E -->|flow| bb_0042EA0F
  bb_0042EA0F -->|branch| bb_0042EA09
```
