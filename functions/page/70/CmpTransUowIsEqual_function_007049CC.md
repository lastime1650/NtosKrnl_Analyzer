# CmpTransUowIsEqual

- RVA: `0x007049CC`–`0x007049E8` (길이 `28` bytes)
- VA: `0x00000001407049CC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007049D6` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)

### Direct callers
- [CmpIsKeyStackDeleted](../84/CmpIsKeyStackDeleted_function_008426E0.md) at `0x00842779`
- [CmEqualTrans](../84/CmEqualTrans_function_0084BF60.md) at `0x0084BF90`
- [CmpWalkOneLevel](../85/CmpWalkOneLevel_function_00852BA0.md) at `0x008532A9`
- [sub_0086FD40](../86/Unknown_function_0086FD40.md) at `0x0086FD6D`
- [sub_0086FDC3](../86/Unknown_function_0086FDC3.md) at `0x0086FE8C`
- [CmpCheckOpenAccessOnKeyBody](../87/CmpCheckOpenAccessOnKeyBody_function_00870000.md) at `0x00870487`
- [CmpCheckOpenAccessOnKeyBody](../87/CmpCheckOpenAccessOnKeyBody_function_00870000.md) at `0x008704C7`
- [CmpCheckOpenAccessOnKeyBody](../87/CmpCheckOpenAccessOnKeyBody_function_00870000.md) at `0x0087053F`
- [CmpCheckOpenAccessOnKeyBody](../87/CmpCheckOpenAccessOnKeyBody_function_00870000.md) at `0x0087092E`
- [CmpSecurityMethod](../87/CmpSecurityMethod_function_00870CC0.md) at `0x00871446`
- [CmpSearchForTrans](../87/CmpSearchForTrans_function_00874B04.md) at `0x00874B56`
- [sub_008C7637](../8C/Unknown_function_008C7637.md) at `0x008C7656`
- [sub_008C7665](../8C/Unknown_function_008C7665.md) at `0x008C76B9`
- [sub_00949E35](../94/Unknown_function_00949E35.md) at `0x00949E98`
- [sub_0099DD1B](../99/Unknown_function_0099DD1B.md) at `0x0099DD3A`
- [sub_0099DD56](../99/Unknown_function_0099DD56.md) at `0x0099DDAA`
- [CmRmIsKcbStackVisible](../9A/CmRmIsKcbStackVisible_function_009A8470.md) at `0x009A84CA`
- [CmRmIsKCBVisible](../9A/CmRmIsKCBVisible_function_009A8510.md) at `0x009A8546`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007049D6` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007049CC  48 83 EC 28                     sub rsp, 0x28
007049D0  41 B8 10 00 00 00               mov r8d, 0x10
007049D6  E8 95 5C FB FF                  call 0x1406ba670
007049DB  48 83 F8 10                     cmp rax, 0x10
007049DF  0F 94 C0                        sete al
007049E2  48 83 C4 28                     add rsp, 0x28
007049E6  C3                              ret
007049E7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpTransUowIsEqual(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = RtlCompareMemory(a1, a2, 16, a4);
    result = (result == 16) ? 1 : 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void CmpTransUowIsEqual(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = RtlCompareMemory(a1, a2, 16, a4);
    result = (result == 16) ? 1 : 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007049CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007049CC[BB_007049CC]
  bb_007049E7[BB_007049E7]
```
