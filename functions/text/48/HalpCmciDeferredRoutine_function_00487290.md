# HalpCmciDeferredRoutine

- RVA: `0x00487290`–`0x004872B6` (길이 `38` bytes)
- VA: `0x0000000140487290`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004872A4` → [HalpCmcStartPolling](../4F/HalpCmcStartPolling_function_004F8D40.md) (function, `0x004F8D40`)
- `0x004872AB` → [HalpCmciPollProcessor](HalpCmciPollProcessor_function_00487A88.md) (function, `0x00487A88`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00487290  48 83 EC 28                     sub rsp, 0x28
00487294  80 BA 80 00 00 00 00            cmp byte ptr [rdx + 0x80], 0
0048729B  48 8B 8A AC 00 00 00            mov rcx, qword ptr [rdx + 0xac]
004872A2  74 07                           je 0x1404872ab
004872A4  E8 97 1A 07 00                  call 0x1404f8d40
004872A9  EB 05                           jmp 0x1404872b0
004872AB  E8 D8 07 00 00                  call 0x140487a88
004872B0  48 83 C4 28                     add rsp, 0x28
004872B4  C3                              ret
004872B5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpCmciDeferredRoutine(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(a2 + 128)) == 0) goto loc_004872AB;
    result = HalpCmcStartPolling(*(unsigned __int64 *)(a2 + 172), a2, a3, a4);
    goto loc_004872B0;
loc_004872AB:
    result = HalpCmciPollProcessor(*(unsigned __int64 *)(a2 + 172), a2, a3, a4);
loc_004872B0:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpCmciDeferredRoutine(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(arg2 + 0x80)) == 0) goto loc_004872AB;
    result = HalpCmcStartPolling(*(uint64_t *)(arg2 + 0xAC), Arg2, a3, a4);
    goto loc_004872B0;
loc_004872AB:
    result = HalpCmciPollProcessor(*(uint64_t *)(arg2 + 0xAC), Arg2, a3, a4);
loc_004872B0:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x80` | `8` | `R` |
| `Arg2` | `+ 0xAC` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00487290&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00487290[BB_00487290]
  bb_004872A4[BB_004872A4]
  bb_004872AB[BB_004872AB]
  bb_004872B0[BB_004872B0]
  bb_004872B5[BB_004872B5]
  bb_00487290 -->|branch| bb_004872AB
  bb_00487290 -->|fallthrough| bb_004872A4
  bb_004872A4 -->|branch| bb_004872B0
  bb_004872AB -->|flow| bb_004872B0
```
