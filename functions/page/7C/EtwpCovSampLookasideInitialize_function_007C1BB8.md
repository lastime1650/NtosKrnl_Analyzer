# EtwpCovSampLookasideInitialize

- RVA: `0x007C1BB8`–`0x007C1C33` (길이 `123` bytes)
- VA: `0x00000001407C1BB8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `36`개 명령, `123/123` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007C1BD9` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007C1C0A` → [InitializeSListHead](../../text/46/InitializeSListHead_function_00468A90.md) (function, `0x00468A90`)

### Direct callers
- [EtwpCovSampCaptureContextStart](EtwpCovSampCaptureContextStart_function_007C14AC.md) at `0x007C1804`
- [EtwpCovSampCaptureContextStart](EtwpCovSampCaptureContextStart_function_007C14AC.md) at `0x007C1813`
- [EtwpCovSampCaptureContextStart](EtwpCovSampCaptureContextStart_function_007C14AC.md) at `0x007C18B5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007C1BD9` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007C1C0A` → [InitializeSListHead](../../text/46/InitializeSListHead_function_00468A90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C1BB8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007C1BBD  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
007C1BC2  57                              push rdi
007C1BC3  48 83 EC 20                     sub rsp, 0x20
007C1BC7  48 8B F2                        mov rsi, rdx
007C1BCA  49 8B F8                        mov rdi, r8
007C1BCD  33 D2                           xor edx, edx
007C1BCF  48 8B D9                        mov rbx, rcx
007C1BD2  48 8B CE                        mov rcx, rsi
007C1BD5  44 8D 42 40                     lea r8d, [rdx + 0x40]
007C1BD9  E8 62 50 F0 FF                  call 0x1406c6c40
007C1BDE  48 81 C3 B0 03 00 00            add rbx, 0x3b0
007C1BE5  48 8D 46 10                     lea rax, [rsi + 0x10]
007C1BE9  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
007C1BED  48 39 19                        cmp qword ptr [rcx], rbx
007C1BF0  74 07                           je 0x1407c1bf9
007C1BF2  B9 03 00 00 00                  mov ecx, 3
007C1BF7  CD 29                           int 0x29
007C1BF9  48 89 48 08                     mov qword ptr [rax + 8], rcx
007C1BFD  48 89 18                        mov qword ptr [rax], rbx
007C1C00  48 89 01                        mov qword ptr [rcx], rax
007C1C03  48 8B CE                        mov rcx, rsi
007C1C06  48 89 43 08                     mov qword ptr [rbx + 8], rax
007C1C0A  E8 81 6E CA FF                  call 0x140468a90
007C1C0F  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
007C1C14  48 89 7E 20                     mov qword ptr [rsi + 0x20], rdi
007C1C18  8B 47 3C                        mov eax, dword ptr [rdi + 0x3c]
007C1C1B  89 46 38                        mov dword ptr [rsi + 0x38], eax
007C1C1E  FF 47 40                        inc dword ptr [rdi + 0x40]
007C1C21  8B 47 3C                        mov eax, dword ptr [rdi + 0x3c]
007C1C24  01 47 44                        add dword ptr [rdi + 0x44], eax
007C1C27  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
007C1C2C  48 83 C4 20                     add rsp, 0x20
007C1C30  5F                              pop rdi
007C1C31  C3                              ret
007C1C32  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpCovSampLookasideInitialize(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a2 = 0;
    result = memset(0, a2, a2 + 64, a4);
    v_rbx = (a1) + (944);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8))) != v_rbx) {
        a1 = 3;
    }
    *(unsigned __int64 *)(a2 + 16 + 8) = a1;
    *(unsigned __int64 *)(a2 + 16) = v_rbx;
    *(unsigned __int64 *)(a1) = a2 + 16;
    *(unsigned __int64 *)(v_rbx + 8) = a2 + 16;
    result = InitializeSListHead(0, a2, a2 + 64, a4);
    *(unsigned __int64 *)(a2 + 32) = a3;
    *(unsigned int *)(a2 + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 60)));
    v_rsp = (v_rsp) + (32);
    return (unsigned int)(*(unsigned int *)(a3 + 60));
}
```

## 5. (Beta) C Style

```c
int64_t EtwpCovSampLookasideInitialize(void *Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    result = memset(0, Arg2, Arg2 + 64, a4);
    local_rbx = (Arg1) + (944);
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8))) != local_rbx) {
        Arg1 = 3;
    }
    *(void **)(arg2 + 0x10 + 0x8) = Arg1;
    *(uint64_t *)(arg2 + 0x10) = local_rbx;
    *(void **)(arg1) = Arg2 + 16;
    *(void **)(local_rbx + 0x8) = Arg2 + 16;
    result = InitializeSListHead(0, Arg2, Arg2 + 64, a4);
    *(void **)(arg2 + 0x20) = Arg3;
    *(uint32_t *)(arg2 + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x3C)));
    local_rsp = (local_rsp) + (32);
    return (uint32_t)(*(uint32_t *)(arg3 + 0x3C));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `W` |
| `Arg2` | `+ 0x38` | `32` | `W` |
| `Arg3` | `+ 0x3C` | `32` | `R` |
| `Arg3` | `+ 0x40` | `32` | `R/W` |
| `Arg3` | `+ 0x44` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C1BB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007C1BB8[BB_007C1BB8]
  bb_007C1BF2[BB_007C1BF2]
  bb_007C1BF9[BB_007C1BF9]
  bb_007C1C32[BB_007C1C32]
  bb_007C1BB8 -->|branch| bb_007C1BF9
  bb_007C1BB8 -->|fallthrough| bb_007C1BF2
  bb_007C1BF2 -->|flow| bb_007C1BF9
```
