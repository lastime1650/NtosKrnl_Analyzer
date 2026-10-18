# I_MincryptFreeChainInfo

- RVA: `0x008395E8`–`0x00839601` (길이 `25` bytes)
- VA: `0x00000001408395E8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008395F6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PopValidateWinresume](../75/PopValidateWinresume_function_0075DFF4.md) at `0x0075E35B`
- [MinCrypK_VerifySignedDataKModeEx](MinCrypK_VerifySignedDataKModeEx_function_00838568.md) at `0x008389C0`
- [I_MincryptAddChainInfo](I_MincryptAddChainInfo_function_00839314.md) at `0x00839356`
- [I_MincryptAddChainInfo](I_MincryptAddChainInfo_function_00839314.md) at `0x008395B9`
- [MincryptFreePolicyInfo](MincryptFreePolicyInfo_function_00839608.md) at `0x0083961E`
- [MinCrypK_VerifySignedDataKModeEx$fin$0](../B1/MinCrypK_VerifySignedDataKModeEx_fin_0_function_00B15DA6.md) at `0x00B15DF2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008395F6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008395E8  48 83 EC 28                     sub rsp, 0x28
008395EC  48 85 C9                        test rcx, rcx
008395EF  74 0A                           je 0x1408395fb
008395F1  BA 43 49 63 72                  mov edx, 0x72634943
008395F6  E8 75 92 34 00                  call 0x140b82870
008395FB  48 83 C4 28                     add rsp, 0x28
008395FF  C3                              ret
00839600  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall I_MincryptFreeChainInfo(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) {
        a2 = 0x72634943ULL;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t I_MincryptFreeChainInfo(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) {
        a2 = 0x72634943ULL;
        result = ExFreePoolWithTag(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008395E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008395E8[BB_008395E8]
  bb_008395F1[BB_008395F1]
  bb_008395FB[BB_008395FB]
  bb_00839600[BB_00839600]
  bb_008395E8 -->|branch| bb_008395FB
  bb_008395E8 -->|fallthrough| bb_008395F1
  bb_008395F1 -->|flow| bb_008395FB
```
