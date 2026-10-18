# ExAcquireRundownProtectionCacheAware

- RVA: `0x0023D110`–`0x0023D151` (길이 `65` bytes)
- VA: `0x000000014023D110`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `20`개 명령, `65/65` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0023D14A` → [ExfAcquireRundownProtection](../34/ExfAcquireRundownProtection_function_0034C050.md) (function, `0x0034C050`)

### Direct callers
- [sub_0023C4C9](Unknown_function_0023C4C9.md) at `0x0023C4E6`
- [sub_00341DB3](../34/Unknown_function_00341DB3.md) at `0x00341F75`
- [sub_003425E5](../34/Unknown_function_003425E5.md) at `0x003426F6`
- [PfpPartitionGetFirst](../34/PfpPartitionGetFirst_function_00342ED0.md) at `0x00343046`
- [PfpPartitionRundownProtectionAcquire](../48/PfpPartitionRundownProtectionAcquire_function_0048402C.md) at `0x00484034`
- [MiSwitchToTransition](../4C/MiSwitchToTransition_function_004C0F5C.md) at `0x004C152F`
- [PfpPartitionCreate](../5C/PfpPartitionCreate_function_005CDE8C.md) at `0x005CDF75`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0023D110  48 83 EC 28                     sub rsp, 0x28
0023D114  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0023D11C  33 D2                           xor edx, edx
0023D11E  F7 71 14                        div dword ptr [rcx + 0x14]
0023D121  4C 8B C1                        mov r8, rcx
0023D124  0F AF 51 10                     imul edx, dword ptr [rcx + 0x10]
0023D128  8B CA                           mov ecx, edx
0023D12A  49 03 08                        add rcx, qword ptr [r8]
0023D12D  0F 0D 09                        prefetchw byte ptr [rcx]
0023D130  48 8B 01                        mov rax, qword ptr [rcx]
0023D133  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0023D137  48 8D 50 02                     lea rdx, [rax + 2]
0023D13B  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
0023D140  75 08                           jne 0x14023d14a
0023D142  B0 01                           mov al, 1
0023D144  48 83 C4 28                     add rsp, 0x28
0023D148  C3                              ret
0023D149  CC                              int3
0023D14A  E8 01 EF 10 00                  call 0x14034c050
0023D14F  EB F3                           jmp 0x14023d144
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExAcquireRundownProtectionCacheAware(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    a2 = (unsigned int)((a2) * (*(unsigned int *)(a1 + 16)));
    a1 = ((unsigned int)(a2)) + (*(unsigned __int64 *)(a1));
    result = (*(unsigned __int64 *)(a1)) & (-2);
    if (condition_is_not_equal) goto loc_0023D14A;
loc_0023D144:
    v_rsp = (v_rsp) + (40);
    return 1;
loc_0023D14A:
    result = ExfAcquireRundownProtection(a1, result + 2, a1, a4);
    goto loc_0023D144;
}
```

## 5. (Beta) C Style

```c
int64_t ExAcquireRundownProtectionCacheAware(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    Arg2 = (uint32_t)((Arg2) * (*(uint32_t *)(arg1 + 0x10)));
    Arg1 = ((uint32_t)(Arg2)) + (*(uint64_t *)(arg1));
    result = (*(uint64_t *)(arg1)) & (-2);
    if (condition_is_not_equal) goto loc_0023D14A;
loc_0023D144:
    local_rsp = (local_rsp) + (40);
    return 1;
loc_0023D14A:
    result = ExfAcquireRundownProtection(Arg1, result + 2, Arg1, a4);
    goto loc_0023D144;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0023D110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0023D110[BB_0023D110]
  bb_0023D142[BB_0023D142]
  bb_0023D144[BB_0023D144]
  bb_0023D149[BB_0023D149]
  bb_0023D14A[BB_0023D14A]
  bb_0023D110 -->|branch| bb_0023D14A
  bb_0023D110 -->|fallthrough| bb_0023D142
  bb_0023D142 -->|flow| bb_0023D144
  bb_0023D149 -->|flow| bb_0023D14A
  bb_0023D14A -->|branch| bb_0023D144
```
