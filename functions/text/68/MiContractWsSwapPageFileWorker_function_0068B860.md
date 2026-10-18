# MiContractWsSwapPageFileWorker

- RVA: `0x0068B860`–`0x0068B942` (길이 `226` bytes)
- VA: `0x000000014068B860`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D6260`
- 디코드: `56`개 명령, `226/226` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0068B87E` → [MiWsSwapPageFileNumber](../2A/MiWsSwapPageFileNumber_function_002A7470.md) (function, `0x002A7470`)
- `0x0068B8A1` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0068B8E5` → [MiLockWsSwapExclusive](../2A/MiLockWsSwapExclusive_function_002A8A70.md) (function, `0x002A8A70`)
- `0x0068B8F0` → [MiQueuePageFileExtension](../48/MiQueuePageFileExtension_function_0048187C.md) (function, `0x0048187C`)
- `0x0068B906` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0068B911` → [MiUnlockWsSwapExclusive](../2A/MiUnlockWsSwapExclusive_function_002A74A8.md) (function, `0x002A74A8`)
- `0x0068B923` → [PsDereferencePartition](../34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0068B860  48 8B C4                        mov rax, rsp
0068B863  48 89 58 08                     mov qword ptr [rax + 8], rbx
0068B867  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0068B86B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0068B86F  55                              push rbp
0068B870  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0068B874  48 81 EC 90 00 00 00            sub rsp, 0x90
0068B87B  48 8B F1                        mov rsi, rcx
0068B87E  E8 ED BB C1 FF                  call 0x1402a7470
0068B883  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
0068B88C  33 D2                           xor edx, edx
0068B88E  44 8B D0                        mov r10d, eax
0068B891  44 8D 42 58                     lea r8d, [rdx + 0x58]
0068B895  4A 8B 9C D1 60 48 00 00         mov rbx, qword ptr [rcx + r10*8 + 0x4860]
0068B89D  48 8D 4D F7                     lea rcx, [rbp - 9]
0068B8A1  E8 9A B3 03 00                  call 0x1406c6c40
0068B8A6  48 83 4D 17 FF                  or qword ptr [rbp + 0x17], 0xffffffffffffffff
0068B8AB  48 8B D6                        mov rdx, rsi
0068B8AE  48 89 75 0F                     mov qword ptr [rbp + 0xf], rsi
0068B8B2  48 8B CF                        mov rcx, rdi
0068B8B5  8A 83 AC 00 00 00               mov al, byte ptr [rbx + 0xac]
0068B8BB  33 DB                           xor ebx, ebx
0068B8BD  24 0F                           and al, 0xf
0068B8BF  48 C7 45 1F 00 00 01 00         mov qword ptr [rbp + 0x1f], 0x10000
0068B8C7  88 45 43                        mov byte ptr [rbp + 0x43], al
0068B8CA  48 8D 45 2F                     lea rax, [rbp + 0x2f]
0068B8CE  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0068B8D2  48 8D 45 2F                     lea rax, [rbp + 0x2f]
0068B8D6  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
0068B8DA  66 89 5D 27                     mov word ptr [rbp + 0x27], bx
0068B8DE  C6 45 29 06                     mov byte ptr [rbp + 0x29], 6
0068B8E2  89 5D 2B                        mov dword ptr [rbp + 0x2b], ebx
0068B8E5  E8 86 D1 C1 FF                  call 0x1402a8a70
0068B8EA  B2 11                           mov dl, 0x11
0068B8EC  48 8D 4D F7                     lea rcx, [rbp - 9]
0068B8F0  E8 87 5F DF FF                  call 0x14048187c
0068B8F5  45 33 C9                        xor r9d, r9d
0068B8F8  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0068B8FD  45 33 C0                        xor r8d, r8d
0068B900  48 8D 4D 27                     lea rcx, [rbp + 0x27]
0068B904  33 D2                           xor edx, edx
0068B906  E8 A5 2D B8 FF                  call 0x14020e6b0
0068B90B  48 8B D6                        mov rdx, rsi
0068B90E  48 8B CF                        mov rcx, rdi
0068B911  E8 92 BB C1 FF                  call 0x1402a74a8
0068B916  87 9E 90 04 00 00               xchg dword ptr [rsi + 0x490], ebx
0068B91C  48 8B 8E B8 00 00 00            mov rcx, qword ptr [rsi + 0xb8]
0068B923  E8 48 75 CB FF                  call 0x140342e70
0068B928  4C 8D 9C 24 90 00 00 00         lea r11, [rsp + 0x90]
0068B930  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
0068B934  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
0068B938  49 8B 7B 20                     mov rdi, qword ptr [r11 + 0x20]
0068B93C  49 8B E3                        mov rsp, r11
0068B93F  5D                              pop rbp
0068B940  C3                              ret
0068B941  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiContractWsSwapPageFileWorker(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (144);
    result = MiWsSwapPageFileNumber(a1, a2, a3, a4);
    a2 = 0;
    result = memset(v_rsp - 95 - 9, a2, a2 + 88, a4);
    *(unsigned __int64 *)(v_rsp - 95 + 15) = a1;
    v_rbx = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + (unsigned int)((unsigned int)(result)) * 8 + 18528) + 172)) & (15));
    *(unsigned __int64 *)(v_rsp - 95 + 31) = 0x10000ULL;
    *(unsigned __int8 *)(v_rsp - 95 + 67) = (unsigned __int8)(result);
    *(unsigned __int64 *)(v_rsp - 95 + 55) = v_rsp - 95 + 47;
    *(unsigned __int64 *)(v_rsp - 95 + 47) = v_rsp - 95 + 47;
    *(unsigned __int16 *)(v_rsp - 95 + 39) = 0;
    *(unsigned __int8 *)(v_rsp - 95 + 41) = 6;
    *(unsigned int *)(v_rsp - 95 + 43) = 0;
    result = MiLockWsSwapExclusive(*(unsigned __int64 *)(gs_base + (0 + 392)), a1, a2 + 88, a4);
    result = MiQueuePageFileExtension(v_rsp - 95 - 9, 17, a2 + 88, a4);
    a4 = 0;
    v_stack_m78 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rsp - 95 + 39, a2, a3, a4);
    result = MiUnlockWsSwapExclusive(*(unsigned __int64 *)(gs_base + (0 + 392)), a1, a3, a4);
    result = PsDereferencePartition(*(unsigned __int64 *)(a1 + 184), a1, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiContractWsSwapPageFileWorker(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m78;
    uint64_t v_stack_m8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (144);
    result = MiWsSwapPageFileNumber(Arg1, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = memset(local_rsp - 95 - 9, Arg2, Arg2 + 88, Arg4);
    *(void **)(local_rsp - 0x5F + 0xF) = Arg1;
    local_rbx = 0;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + (uint32_t)((uint32_t)(result)) * 8 + 0x4860) + 0xAC)) & (15));
    *(uint64_t *)(local_rsp - 0x5F + 0x1F) = 0x10000ULL;
    *(uint8_t *)(local_rsp - 0x5F + 0x43) = (uint8_t)(result);
    *(uint64_t *)(local_rsp - 0x5F + 0x37) = local_rsp - 95 + 47;
    *(uint64_t *)(local_rsp - 0x5F + 0x2F) = local_rsp - 95 + 47;
    *(uint16_t *)(local_rsp - 0x5F + 0x27) = 0;
    *(uint8_t *)(local_rsp - 0x5F + 0x29) = 6;
    *(uint32_t *)(local_rsp - 0x5F + 0x2B) = 0;
    result = MiLockWsSwapExclusive(*(uint64_t *)(gs_base + (0 + 0x188)), Arg1, Arg2 + 88, Arg4);
    result = MiQueuePageFileExtension(local_rsp - 95 - 9, 17, Arg2 + 88, Arg4);
    Arg4 = 0;
    v_stack_m78 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(local_rsp - 95 + 39, Arg2, Arg3, Arg4);
    result = MiUnlockWsSwapExclusive(*(uint64_t *)(gs_base + (0 + 0x188)), Arg1, Arg3, Arg4);
    result = PsDereferencePartition(*(uint64_t *)(arg1 + 0xB8), Arg1, Arg3, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0x490` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0068B860&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0068B860[BB_0068B860]
  bb_0068B941[BB_0068B941]
```
