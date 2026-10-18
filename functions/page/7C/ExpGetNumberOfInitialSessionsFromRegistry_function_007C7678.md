# ExpGetNumberOfInitialSessionsFromRegistry

- RVA: `0x007C7678`–`0x007C76F6` (길이 `126` bytes)
- VA: `0x00000001407C7678`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CE364`
- 디코드: `29`개 명령, `126/126` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x007C7694` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007C76DA` → [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) (function, `0x008C9050`)

### Direct callers
- [ExIsMultiSessionSku](ExIsMultiSessionSku_function_007C7538.md) at `0x007C7574`

### Static image references
- `0x007C76A4` → RVA `0x00B086A0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007C76D3` → RVA `0x00B08680` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007C7694` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C7678  48 8B C4                        mov rax, rsp
007C767B  53                              push rbx
007C767C  48 81 EC A0 00 00 00            sub rsp, 0xa0
007C7683  83 60 10 00                     and dword ptr [rax + 0x10], 0
007C7687  33 D2                           xor edx, edx
007C7689  48 8B D9                        mov rbx, rcx
007C768C  48 8D 48 88                     lea rcx, [rax - 0x78]
007C7690  44 8D 42 70                     lea r8d, [rdx + 0x70]
007C7694  E8 A7 F5 EF FF                  call 0x1406c6c40
007C7699  45 33 C9                        xor r9d, r9d
007C769C  C7 44 24 38 24 01 00 00         mov dword ptr [rsp + 0x38], 0x124
007C76A4  48 8D 05 F5 0F 34 00            lea rax, [rip + 0x340ff5]
007C76AB  C7 44 24 50 04 00 00 04         mov dword ptr [rsp + 0x50], 0x4000004
007C76B3  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
007C76B8  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
007C76BD  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
007C76C5  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
007C76CA  41 8D 49 02                     lea ecx, [r9 + 2]
007C76CE  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007C76D3  48 8D 15 A6 0F 34 00            lea rdx, [rip + 0x340fa6]
007C76DA  E8 71 19 10 00                  call 0x1408c9050
007C76DF  85 C0                           test eax, eax
007C76E1  78 09                           js 0x1407c76ec
007C76E3  8B 8C 24 B8 00 00 00            mov ecx, dword ptr [rsp + 0xb8]
007C76EA  89 0B                           mov dword ptr [rbx], ecx
007C76EC  48 81 C4 A0 00 00 00            add rsp, 0xa0
007C76F3  5B                              pop rbx
007C76F4  C3                              ret
007C76F5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpGetNumberOfInitialSessionsFromRegistry(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int8 v_stack_m80;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (160);
    a2 = 0;
    result = memset(v_rsp - 120, a2, a2 + 112, a4);
    a4 = 0;
    v_stack_m70 = 292;
    v_stack_m58 = 0x4000004ULL;
    v_stack_m68 = v_rip + 3411957;
    v_stack_m80 = 1;
    v_stack_m60 = v_stack_p10;
    result = RtlpQueryRegistryValues(a4 + 2, v_rip + 3411878, v_stack_m78, a4);
    if (!(sign_flag)) {
        a1 = v_stack_p10;
        *(unsigned int *)(a1) = (unsigned int)(a1);
    }
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpGetNumberOfInitialSessionsFromRegistry(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint8_t v_stack_m80;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (160);
    Arg2 = 0;
    result = memset(local_rsp - 120, Arg2, Arg2 + 112, Arg4);
    Arg4 = 0;
    v_stack_m70 = 292;
    v_stack_m58 = 0x4000004ULL;
    v_stack_m68 = v_rip + 3411957;
    v_stack_m80 = 1;
    v_stack_m60 = v_stack_p10;
    result = RtlpQueryRegistryValues(Arg4 + 2, v_rip + 3411878, v_stack_m78, Arg4);
    if (!(sign_flag)) {
        Arg1 = v_stack_p10;
        *(uint32_t *)(arg1) = (uint32_t)(Arg1);
    }
    local_rsp = (local_rsp) + (160);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C7678&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007C7678[BB_007C7678]
  bb_007C76E3[BB_007C76E3]
  bb_007C76EC[BB_007C76EC]
  bb_007C76F5[BB_007C76F5]
  bb_007C7678 -->|branch| bb_007C76EC
  bb_007C7678 -->|fallthrough| bb_007C76E3
  bb_007C76E3 -->|flow| bb_007C76EC
```
