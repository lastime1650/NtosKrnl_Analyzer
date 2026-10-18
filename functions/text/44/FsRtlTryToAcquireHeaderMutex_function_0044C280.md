# FsRtlTryToAcquireHeaderMutex

- RVA: `0x0044C280`–`0x0044C2B2` (길이 `50` bytes)
- VA: `0x000000014044C280`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00085914`
- 디코드: `15`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0044C291` → [ExTryToAcquireFastMutex](ExTryToAcquireFastMutex_function_0044C2E0.md) (function, `0x0044C2E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0044C280  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0044C285  48 83 EC 28                     sub rsp, 0x28
0044C289  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
0044C28D  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0044C291  E8 4A 00 00 00                  call 0x14044c2e0
0044C296  84 C0                           test al, al
0044C298  74 12                           je 0x14044c2ac
0044C29A  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0044C29F  48 85 C9                        test rcx, rcx
0044C2A2  74 08                           je 0x14044c2ac
0044C2A4  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0044C2A9  F0 FF 01                        lock inc dword ptr [rcx]
0044C2AC  48 83 C4 28                     add rsp, 0x28
0044C2B0  C3                              ret
0044C2B1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlTryToAcquireHeaderMutex(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (40);
    result = ExTryToAcquireFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 48), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0044C2AC;
    if (v_stack_p10 != 0) {
        a1 = v_stack_p10;
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlTryToAcquireHeaderMutex(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (40);
    result = ExTryToAcquireFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30), Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0044C2AC;
    if (v_stack_p10 != 0) {
        Arg1 = v_stack_p10;
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044C280&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044C280[BB_0044C280]
  bb_0044C29A[BB_0044C29A]
  bb_0044C2A4[BB_0044C2A4]
  bb_0044C2AC[BB_0044C2AC]
  bb_0044C2B1[BB_0044C2B1]
  bb_0044C280 -->|branch| bb_0044C2AC
  bb_0044C280 -->|fallthrough| bb_0044C29A
  bb_0044C29A -->|branch| bb_0044C2AC
  bb_0044C29A -->|fallthrough| bb_0044C2A4
  bb_0044C2A4 -->|flow| bb_0044C2AC
```
