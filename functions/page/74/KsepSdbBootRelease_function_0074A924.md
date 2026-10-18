# KsepSdbBootRelease

- RVA: `0x0074A924`–`0x0074A958` (길이 `52` bytes)
- VA: `0x000000014074A924`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `17`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0074A935` → [SdbReleaseDatabase](../95/SdbReleaseDatabase_function_0095B57C.md) (function, `0x0095B57C`)
- `0x0074A947` → [KsepPoolFreePaged](../../text/4B/KsepPoolFreePaged_function_004B0E10.md) (function, `0x004B0E10`)

### Direct callers
- [KseShimDatabaseBootRelease](../95/KseShimDatabaseBootRelease_function_00959174.md) at `0x009591F4`
- [KseShimDatabaseBootRelease](../95/KseShimDatabaseBootRelease_function_00959174.md) at `0x00959200`
- [KseShimDatabaseBootInitialize](../../init/C3/KseShimDatabaseBootInitialize_function_00C3C124.md) at `0x00C3C283`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0074A947` → [KsepPoolFreePaged](../../text/4B/KsepPoolFreePaged_function_004B0E10.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0074A924  40 53                           push rbx
0074A926  48 83 EC 20                     sub rsp, 0x20
0074A92A  48 8B D9                        mov rbx, rcx
0074A92D  48 8B 09                        mov rcx, qword ptr [rcx]
0074A930  48 85 C9                        test rcx, rcx
0074A933  74 09                           je 0x14074a93e
0074A935  E8 42 0C 21 00                  call 0x14095b57c
0074A93A  48 83 23 00                     and qword ptr [rbx], 0
0074A93E  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0074A942  48 85 C9                        test rcx, rcx
0074A945  74 0A                           je 0x14074a951
0074A947  E8 C4 64 D6 FF                  call 0x1404b0e10
0074A94C  48 83 63 08 00                  and qword ptr [rbx + 8], 0
0074A951  48 83 C4 20                     add rsp, 0x20
0074A955  5B                              pop rbx
0074A956  C3                              ret
0074A957  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepSdbBootRelease(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1) != 0) {
        result = SdbReleaseDatabase(*(unsigned __int64 *)(a1), a2, a3, a4);
    }
    if (*(unsigned __int64 *)(a1 + 8) != 0) {
        result = KsepPoolFreePaged(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KsepSdbBootRelease(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1) != 0) {
        result = SdbReleaseDatabase(*(uint64_t *)(arg1), a2, a3, a4);
    }
    if (*(uint64_t *)(arg1 + 0x8) != 0) {
        result = KsepPoolFreePaged(*(uint64_t *)(arg1 + 0x8), a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0074A924&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0074A924[BB_0074A924]
  bb_0074A935[BB_0074A935]
  bb_0074A93E[BB_0074A93E]
  bb_0074A947[BB_0074A947]
  bb_0074A951[BB_0074A951]
  bb_0074A957[BB_0074A957]
  bb_0074A924 -->|branch| bb_0074A93E
  bb_0074A924 -->|fallthrough| bb_0074A935
  bb_0074A935 -->|flow| bb_0074A93E
  bb_0074A93E -->|branch| bb_0074A951
  bb_0074A93E -->|fallthrough| bb_0074A947
  bb_0074A947 -->|flow| bb_0074A951
```
