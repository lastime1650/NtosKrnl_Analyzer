# CmFcpReleaseUsageProviderSubscription

- RVA: `0x0066B3DC`–`0x0066B413` (길이 `55` bytes)
- VA: `0x000000014066B3DC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `16`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0066B408` → [CmFcpManagerFreeUsageProviderSubscription](../../page/70/CmFcpManagerFreeUsageProviderSubscription_function_007056E0.md) (function, `0x007056E0`)

### Direct callers
- [CmFcpUsageProviderWorkItemWrapper](CmFcpUsageProviderWorkItemWrapper_function_0066B500.md) at `0x0066B53C`
- [CmFcManagerUnregisterFeatureUsageProvider](../../page/7F/CmFcManagerUnregisterFeatureUsageProvider_function_007F4ABC.md) at `0x007F4C14`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0066B408` → [CmFcpManagerFreeUsageProviderSubscription](../../page/70/CmFcpManagerFreeUsageProviderSubscription_function_007056E0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066B3DC  48 83 EC 28                     sub rsp, 0x28
0066B3E0  48 83 C8 FF                     or rax, 0xffffffffffffffff
0066B3E4  F0 48 0F C1 81 88 00 00 00      lock xadd qword ptr [rcx + 0x88], rax
0066B3ED  48 83 E8 01                     sub rax, 1
0066B3F1  7F 1A                           jg 0x14066b40d
0066B3F3  48 85 C0                        test rax, rax
0066B3F6  74 09                           je 0x14066b401
0066B3F8  B9 0E 00 00 00                  mov ecx, 0xe
0066B3FD  CD 29                           int 0x29
0066B3FF  EB 0C                           jmp 0x14066b40d
0066B401  48 8B D1                        mov rdx, rcx
0066B404  48 8B 49 58                     mov rcx, qword ptr [rcx + 0x58]
0066B408  E8 D3 A2 09 00                  call 0x1407056e0
0066B40D  48 83 C4 28                     add rsp, 0x28
0066B411  C3                              ret
0066B412  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmFcpReleaseUsageProviderSubscription(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (result) | (-1);
    result = (result) - (1);
    if (condition_is_greater) goto loc_0066B40D;
    if (result == 0) goto loc_0066B401;
    goto loc_0066B40D;
loc_0066B401:
    result = CmFcpManagerFreeUsageProviderSubscription(*(unsigned __int64 *)(14 + 88), 14, a3, a4);
loc_0066B40D:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmFcpReleaseUsageProviderSubscription(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (result) | (-1);
    result = (result) - (1);
    if (condition_is_greater) goto loc_0066B40D;
    if (result == 0) goto loc_0066B401;
    goto loc_0066B40D;
loc_0066B401:
    result = CmFcpManagerFreeUsageProviderSubscription(*(uint64_t *)(14 + 0x58), 14, a3, a4);
loc_0066B40D:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x88` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066B3DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066B3DC[BB_0066B3DC]
  bb_0066B3F3[BB_0066B3F3]
  bb_0066B3F8[BB_0066B3F8]
  bb_0066B401[BB_0066B401]
  bb_0066B40D[BB_0066B40D]
  bb_0066B412[BB_0066B412]
  bb_0066B3DC -->|branch| bb_0066B40D
  bb_0066B3DC -->|fallthrough| bb_0066B3F3
  bb_0066B3F3 -->|branch| bb_0066B401
  bb_0066B3F3 -->|fallthrough| bb_0066B3F8
  bb_0066B3F8 -->|branch| bb_0066B40D
  bb_0066B401 -->|flow| bb_0066B40D
```
