# PpmInfoReleaseLocks

- RVA: `0x00916154`–`0x0091617E` (길이 `42` bytes)
- VA: `0x0000000140916154`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C74`
- 디코드: `11`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00916165` → [PpmReleaseLock](../../text/2D/PpmReleaseLock_function_002DA428.md) (function, `0x002DA428`)
- `0x00916177` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)

### Direct callers
- [PpmSetProfilePolicySetting](PpmSetProfilePolicySetting_function_00915A44.md) at `0x00915F30`
- [PpmInfoApplySettingUpdate](PpmInfoApplySettingUpdate_function_009160A8.md) at `0x009160DD`

### Static image references
- `0x0091615E` → RVA `0x00F0CC00` (`.data`; read)
- `0x00916170` → RVA `0x00F0CA70` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00916165` → [PpmReleaseLock](../../text/2D/PpmReleaseLock_function_002DA428.md) (`PAGE` → `.text`)
  - `0x00916177` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00916154  48 83 EC 28                     sub rsp, 0x28
00916158  F6 41 25 01                     test byte ptr [rcx + 0x25], 1
0091615C  74 12                           je 0x140916170
0091615E  48 8D 0D 9B 6A 5F 00            lea rcx, [rip + 0x5f6a9b]
00916165  E8 BE 42 9C FF                  call 0x1402da428
0091616A  48 83 C4 28                     add rsp, 0x28
0091616E  C3                              ret
0091616F  CC                              int3
00916170  48 8D 0D F9 68 5F 00            lea rcx, [rip + 0x5f68f9]
00916177  E8 40 9A 9C FF                  call 0x1402dfbbc
0091617C  EB EC                           jmp 0x14091616a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmInfoReleaseLocks(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((*(unsigned __int8 *)(a1 + 37)) & (1)) == 0) goto loc_00916170;
    result = PpmReleaseLock(v_rip + 6253211, a2, a3, a4);
loc_0091616A:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00916170:
    result = PopReleaseRwLock(v_rip + 6252793, a2, a3, a4);
    goto loc_0091616A;
}
```

## 5. (Beta) C Style

```c
int64_t PpmInfoReleaseLocks(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((*(uint8_t *)(arg1 + 0x25)) & (1)) == 0) goto loc_00916170;
    result = PpmReleaseLock(v_rip + 6253211, a2, a3, a4);
loc_0091616A:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00916170:
    result = PopReleaseRwLock(v_rip + 6252793, a2, a3, a4);
    goto loc_0091616A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x25` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00916154&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00916154[BB_00916154]
  bb_0091615E[BB_0091615E]
  bb_0091616A[BB_0091616A]
  bb_0091616F[BB_0091616F]
  bb_00916170[BB_00916170]
  bb_00916154 -->|branch| bb_00916170
  bb_00916154 -->|fallthrough| bb_0091615E
  bb_0091615E -->|flow| bb_0091616A
  bb_0091616F -->|flow| bb_00916170
  bb_00916170 -->|branch| bb_0091616A
```
