# PfSnAsyncContextInitialize

- RVA: `0x00961168`–`0x0096122E` (길이 `198` bytes)
- VA: `0x0000000140961168`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008D180`
- 디코드: `43`개 명령, `198/198` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00961191` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009611B8` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x009611C4` → [PfSnReferenceProcessTrace](../../text/34/PfSnReferenceProcessTrace_function_00344A80.md) (function, `0x00344A80`)
- `0x009611E1` → [PsGetPagePriorityThread](../../text/3C/PsGetPagePriorityThread_function_003C3E80.md) (function, `0x003C3E80`)
- `0x00961208` → [PfSnPowerBoostInitialize](PfSnPowerBoostInitialize_function_00961348.md) (function, `0x00961348`)

### Direct callers
- [PfSnPrefetchScenario](PfSnPrefetchScenario_function_00961080.md) at `0x009610EA`

### Static image references
- `0x009611ED` → RVA `0x009394B0` (`PfSnAsyncPrefetchWorker`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00961191` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009611B8` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x009611C4` → [PfSnReferenceProcessTrace](../../text/34/PfSnReferenceProcessTrace_function_00344A80.md) (`PAGE` → `.text`)
  - `0x009611E1` → [PsGetPagePriorityThread](../../text/3C/PsGetPagePriorityThread_function_003C3E80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00961168  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0096116D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00961172  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
00961177  41 56                           push r14
00961179  48 83 EC 20                     sub rsp, 0x20
0096117D  49 8B F8                        mov rdi, r8
00961180  48 8B DA                        mov rbx, rdx
00961183  33 D2                           xor edx, edx
00961185  41 B8 F8 00 00 00               mov r8d, 0xf8
0096118B  41 8B F1                        mov esi, r9d
0096118E  4C 8B F1                        mov r14, rcx
00961191  E8 AA 5A D6 FF                  call 0x1406c6c40
00961196  49 89 9E D0 00 00 00            mov qword ptr [r14 + 0xd0], rbx
0096119D  49 89 7E 20                     mov qword ptr [r14 + 0x20], rdi
009611A1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009611AA  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009611B1  49 89 8E D8 00 00 00            mov qword ptr [r14 + 0xd8], rcx
009611B8  E8 63 E8 8A FF                  call 0x14020fa20
009611BD  49 8B 8E D8 00 00 00            mov rcx, qword ptr [r14 + 0xd8]
009611C4  E8 B7 38 9E FF                  call 0x140344a80
009611C9  49 89 86 E0 00 00 00            mov qword ptr [r14 + 0xe0], rax
009611D0  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
009611D4  48 83 20 00                     and qword ptr [rax], 0
009611D8  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009611E1  E8 9A 2C A6 FF                  call 0x1403c3e80
009611E6  41 89 86 EC 00 00 00            mov dword ptr [r14 + 0xec], eax
009611ED  48 8D 05 BC 82 FD FF            lea rax, [rip - 0x27d44]
009611F4  49 83 26 00                     and qword ptr [r14], 0
009611F8  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
009611FC  4D 89 76 18                     mov qword ptr [r14 + 0x18], r14
00961200  85 F6                           test esi, esi
00961202  75 20                           jne 0x140961224
00961204  49 8D 4E 28                     lea rcx, [r14 + 0x28]
00961208  E8 3B 01 00 00                  call 0x140961348
0096120D  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00961212  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00961217  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
0096121C  48 83 C4 20                     add rsp, 0x20
00961220  41 5E                           pop r14
00961222  C3                              ret
00961223  CC                              int3
00961224  41 83 8E F0 00 00 00 01         or dword ptr [r14 + 0xf0], 1
0096122C  EB D6                           jmp 0x140961204
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfSnAsyncContextInitialize(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (32);
    a2 = 0;
    result = memset(a1, a2, 248, a4);
    *(unsigned __int64 *)(a1 + 208) = 0;
    *(unsigned __int64 *)(a1 + 32) = a3;
    *(unsigned __int64 *)(a1 + 216) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    result = ObfReferenceObject(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, 248, a4);
    result = PfSnReferenceProcessTrace(*(unsigned __int64 *)(a1 + 216), a2, 248, a4);
    *(unsigned __int64 *)(a1 + 224) = result;
    result = PsGetPagePriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, 248, a4);
    *(unsigned int *)(a1 + 236) = (unsigned int)(result);
    *(unsigned __int64 *)(a1 + 16) = v_rip - 163140;
    *(unsigned __int64 *)(a1 + 24) = a1;
    if ((unsigned int)((unsigned int)(a4)) != 0) goto loc_00961224;
loc_00961204:
    result = PfSnPowerBoostInitialize(a1 + 40, a2, 248, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_00961224:
    goto loc_00961204;
}
```

## 5. (Beta) C Style

```c
int64_t PfSnAsyncContextInitialize(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    result = memset(Arg1, Arg2, 248, Arg4);
    *(uint64_t *)(arg1 + 0xD0) = 0;
    *(uint64_t *)(arg1 + 0x20) = Arg3;
    *(uint64_t *)(arg1 + 0xD8) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    result = ObfReferenceObject(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, 248, Arg4);
    result = PfSnReferenceProcessTrace(*(uint64_t *)(arg1 + 0xD8), Arg2, 248, Arg4);
    *(uint64_t *)(arg1 + 0xE0) = result;
    result = PsGetPagePriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, 248, Arg4);
    *(uint32_t *)(arg1 + 0xEC) = (uint32_t)(result);
    *(uint64_t *)(arg1 + 0x10) = v_rip - 163140;
    *(void **)(arg1 + 0x18) = Arg1;
    if ((uint32_t)((uint32_t)(Arg4)) != 0) goto loc_00961224;
loc_00961204:
    result = PfSnPowerBoostInitialize(Arg1 + 40, Arg2, 248, Arg4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_00961224:
    goto loc_00961204;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0xD0` | `64` | `W` |
| `Arg1` | `+ 0xD8` | `64` | `R` |
| `Arg1` | `+ 0xD8` | `64` | `W` |
| `Arg1` | `+ 0xE0` | `64` | `W` |
| `Arg1` | `+ 0xEC` | `32` | `W` |
| `Arg1` | `+ 0xF0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00961168&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00961168[BB_00961168]
  bb_00961204[BB_00961204]
  bb_00961223[BB_00961223]
  bb_00961224[BB_00961224]
  bb_00961168 -->|branch| bb_00961224
  bb_00961168 -->|fallthrough| bb_00961204
  bb_00961223 -->|flow| bb_00961224
  bb_00961224 -->|branch| bb_00961204
```
