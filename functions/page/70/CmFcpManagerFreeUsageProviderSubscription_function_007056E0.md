# CmFcpManagerFreeUsageProviderSubscription

- RVA: `0x007056E0`–`0x0070570F` (길이 `47` bytes)
- VA: `0x00000001407056E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00705704` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [CmFcpReleaseUsageProviderSubscription](../../text/66/CmFcpReleaseUsageProviderSubscription_function_0066B3DC.md) at `0x0066B408`
- [CmFcManagerUnregisterFeatureUsageProvider](../7F/CmFcManagerUnregisterFeatureUsageProvider_function_007F4ABC.md) at `0x007F4CDD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00705704` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007056E0  48 83 EC 28                     sub rsp, 0x28
007056E4  48 8D 81 D0 03 00 00            lea rax, [rcx + 0x3d0]
007056EB  4C 8B C2                        mov r8, rdx
007056EE  48 3B D0                        cmp rdx, rax
007056F1  72 0C                           jb 0x1407056ff
007056F3  48 8D 81 80 05 00 00            lea rax, [rcx + 0x580]
007056FA  48 3B D0                        cmp rdx, rax
007056FD  72 0A                           jb 0x140705709
007056FF  33 D2                           xor edx, edx
00705701  49 8B C8                        mov rcx, r8
00705704  E8 67 D1 47 00                  call 0x140b82870
00705709  48 83 C4 28                     add rsp, 0x28
0070570D  C3                              ret
0070570E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmFcpManagerFreeUsageProviderSubscription(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 < (a1 + 976)) goto loc_007056FF;
    result = a1 + 1408;
    if (a2 >= (a1 + 1408)) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a2, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmFcpManagerFreeUsageProviderSubscription(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 < (Arg1 + 976)) goto loc_007056FF;
    result = Arg1 + 1408;
    if (Arg2 >= (Arg1 + 1408)) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg2, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x3D0` | `64` | `R` |
| `Arg1` | `+ 0x580` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007056E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007056E0[BB_007056E0]
  bb_007056F3[BB_007056F3]
  bb_007056FF[BB_007056FF]
  bb_00705709[BB_00705709]
  bb_0070570E[BB_0070570E]
  bb_007056E0 -->|branch| bb_007056FF
  bb_007056E0 -->|fallthrough| bb_007056F3
  bb_007056F3 -->|branch| bb_00705709
  bb_007056F3 -->|fallthrough| bb_007056FF
  bb_007056FF -->|flow| bb_00705709
```
