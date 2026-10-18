# HalpDmaNextContiguousPiece

- RVA: `0x003DECB0`–`0x003DECF4` (길이 `68` bytes)
- VA: `0x00000001403DECB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000946B8`
- 디코드: `19`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003DECD2` → [HalpDmaNextContiguousPieceV3](HalpDmaNextContiguousPieceV3_function_003DECFC.md) (function, `0x003DECFC`)
- `0x003DECED` → [HalpDmaNextContiguousPieceV2](HalpDmaNextContiguousPieceV2_function_003DE530.md) (function, `0x003DE530`)

### Direct callers
- [HalpDmaFlushContiguousTransferV3](HalpDmaFlushContiguousTransferV3_function_003D9E70.md) at `0x003D9EAD`
- [HalpDmaFlushScatterTransferV3](HalpDmaFlushScatterTransferV3_function_003DB06C.md) at `0x003DB105`
- [sub_003DEA82](Unknown_function_003DEA82.md) at `0x003DEB2F`
- [HalpDmaMapContiguousTransferV2](HalpDmaMapContiguousTransferV2_function_003DFDF4.md) at `0x003DFE37`
- [HalpDmaFlushContiguousTransferV2](HalpDmaFlushContiguousTransferV2_function_003DFF3C.md) at `0x003DFF7B`
- [IoFlushAdapterBuffersV2](../3E/IoFlushAdapterBuffersV2_function_003E0050.md) at `0x003E0148`
- [HalpDmaMapScatterTransferV3](../4A/HalpDmaMapScatterTransferV3_function_004A1EDC.md) at `0x004A1F1F`
- [HalpDmaMapContiguousTransferV3](../4D/HalpDmaMapContiguousTransferV3_function_004D6C38.md) at `0x004D6C7A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003DECB0  48 83 EC 38                     sub rsp, 0x38
003DECB4  8B 81 9C 00 00 00               mov eax, dword ptr [rcx + 0x9c]
003DECBA  83 F8 02                        cmp eax, 2
003DECBD  74 1E                           je 0x1403decdd
003DECBF  83 F8 03                        cmp eax, 3
003DECC2  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
003DECC6  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
003DECCA  8A 44 24 60                     mov al, byte ptr [rsp + 0x60]
003DECCE  88 44 24 20                     mov byte ptr [rsp + 0x20], al
003DECD2  E8 25 00 00 00                  call 0x1403decfc
003DECD7  48 83 C4 38                     add rsp, 0x38
003DECDB  C3                              ret
003DECDC  CC                              int3
003DECDD  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
003DECE1  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
003DECE5  8A 44 24 60                     mov al, byte ptr [rsp + 0x60]
003DECE9  88 44 24 20                     mov byte ptr [rsp + 0x20], al
003DECED  E8 3E F8 FF FF                  call 0x1403de530
003DECF2  EB E3                           jmp 0x1403decd7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpDmaNextContiguousPiece(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned __int8 v_stack_m18;
    unsigned __int8 v_stack_p20;
    unsigned int v_stack_p28;

    v_rsp = (v_rsp) - (56);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 156)))) == 2) goto loc_003DECDD;
    v_stack_m10 = (unsigned int)((unsigned int)(a6));
    v_stack_m18 = a5;
    result = HalpDmaNextContiguousPieceV3(a1, a2, a3, a4);
loc_003DECD7:
    v_rsp = (v_rsp) + (56);
    return result;
loc_003DECDD:
    v_stack_p28 = (unsigned int)((unsigned int)(a6));
    v_stack_p20 = a5;
    result = HalpDmaNextContiguousPieceV2(a1, a2, a3, a4);
    goto loc_003DECD7;
}
```

## 5. (Beta) C Style

```c
int64_t HalpDmaNextContiguousPiece(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5, uint32_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint8_t v_stack_m18;
    uint8_t v_stack_p20;
    uint32_t v_stack_p28;

    local_rsp = (local_rsp) - (56);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9C)))) == 2) goto loc_003DECDD;
    v_stack_m10 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m18 = Arg5;
    result = HalpDmaNextContiguousPieceV3(Arg1, Arg2, Arg3, Arg4);
loc_003DECD7:
    local_rsp = (local_rsp) + (56);
    return result;
loc_003DECDD:
    v_stack_p28 = (uint32_t)((uint32_t)(Arg6));
    v_stack_p20 = Arg5;
    result = HalpDmaNextContiguousPieceV2(Arg1, Arg2, Arg3, Arg4);
    goto loc_003DECD7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x9C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003DECB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003DECB0[BB_003DECB0]
  bb_003DECBF[BB_003DECBF]
  bb_003DECD7[BB_003DECD7]
  bb_003DECDC[BB_003DECDC]
  bb_003DECDD[BB_003DECDD]
  bb_003DECB0 -->|branch| bb_003DECDD
  bb_003DECB0 -->|fallthrough| bb_003DECBF
  bb_003DECBF -->|flow| bb_003DECD7
  bb_003DECDC -->|flow| bb_003DECDD
  bb_003DECDD -->|branch| bb_003DECD7
```
