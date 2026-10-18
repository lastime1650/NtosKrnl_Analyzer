# sub_006D7070

- RVA: `0x006D7070`–`0x006D7131` (길이 `193` bytes)
- VA: `0x00000001406D7070`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005FD54`
- 디코드: `43`개 명령, `193/193` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D7088` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x006D709D` → [MiUpdatePfnPriority](../2B/MiUpdatePfnPriority_function_002B8570.md) (function, `0x002B8570`)
- `0x006D70AC` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x006D70B6` → [MiMakePrototypePteDirect](../29/MiMakePrototypePteDirect_function_00294DE0.md) (function, `0x00294DE0`)
- `0x006D70C6` → [MiWriteRepurposedTransitionPte](../4B/MiWriteRepurposedTransitionPte_function_004B0EC8.md) (function, `0x004B0EC8`)
- `0x006D70EA` → [MiPfnReferenceCountIsZero](../2B/MiPfnReferenceCountIsZero_function_002B9E40.md) (function, `0x002B9E40`)
- `0x006D711E` → [MiLockAndDecrementShareCount](../2A/MiLockAndDecrementShareCount_function_002A2854.md) (function, `0x002A2854`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006D712C` → [MiCombineWithStandbyExisting + 0xF9](../22/MiCombineWithStandbyExisting_function_00229E74.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006D7070  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
006D7074  48 B9 00 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000000
006D707E  48 23 C1                        and rax, rcx
006D7081  48 8B CD                        mov rcx, rbp
006D7084  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
006D7088  E8 63 B6 C4 FF                  call 0x1403226f0
006D708D  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
006D7095  45 33 C0                        xor r8d, r8d
006D7098  48 8B CB                        mov rcx, rbx
006D709B  8B D0                           mov edx, eax
006D709D  E8 CE 14 BE FF                  call 0x1402b8570
006D70A2  F0 4C 21 73 18                  lock and qword ptr [rbx + 0x18], r14
006D70A7  B2 12                           mov dl, 0x12
006D70A9  49 8B CF                        mov rcx, r15
006D70AC  E8 DF EF B6 FF                  call 0x140246090
006D70B1  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
006D70B6  E8 25 DD BB FF                  call 0x140294de0
006D70BB  48 0F BA E8 0B                  bts rax, 0xb
006D70C0  48 8B CD                        mov rcx, rbp
006D70C3  48 8B D0                        mov rdx, rax
006D70C6  E8 FD 9D DD FF                  call 0x1404b0ec8
006D70CB  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
006D70CF  48 B9 00 00 00 00 00 00 00 40   movabs rcx, 0x4000000000000000
006D70D9  48 0B C1                        or rax, rcx
006D70DC  49 8B D4                        mov rdx, r12
006D70DF  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
006D70E3  48 8B CD                        mov rcx, rbp
006D70E6  48 8B 5D 28                     mov rbx, qword ptr [rbp + 0x28]
006D70EA  E8 51 2D BE FF                  call 0x1402b9e40
006D70EF  F0 4C 21 75 18                  lock and qword ptr [rbp + 0x18], r14
006D70F4  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
006D70FE  48 23 D8                        and rbx, rax
006D7101  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
006D710B  48 8D 0C 5B                     lea rcx, [rbx + rbx*2]
006D710F  48 C1 E1 04                     shl rcx, 4
006D7113  48 8B C0                        mov rax, rax
006D7116  48 03 C8                        add rcx, rax
006D7119  BA 02 00 00 00                  mov edx, 2
006D711E  E8 31 B7 BC FF                  call 0x1402a2854
006D7123  49 8B 45 68                     mov rax, qword ptr [r13 + 0x68]
006D7127  48 FF 00                        inc qword ptr [rax]
006D712A  33 C0                           xor eax, eax
006D712C  E9 3C 2E B5 FF                  jmp 0x140229f6d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006D7070(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17)
{
    __int64 result;
    __int64 v_rbx;
    unsigned __int64 v_stack_p20;

    result = (*(unsigned __int64 *)(v_rbp + 24)) & (a1);
    *(unsigned __int64 *)(v_rbp + 24) = result;
    result = MiGetPfnPriority(v_rbp, a2, a3, a4);
    a3 = 0;
    result = MiUpdatePfnPriority(a17, (unsigned int)((unsigned int)(result)), a3, a4);
    result = MiUnlockProtoPoolPage(v_r15, 18, a3, a4);
    result = MiMakePrototypePteDirect(v_stack_p20, 18, a3, a4);
    result = MiWriteRepurposedTransitionPte(v_rbp, result, a3, a4);
    result = (*(unsigned __int64 *)(v_rbp + 24)) | (v_rbp);
    *(unsigned __int64 *)(v_rbp + 24) = result;
    result = MiPfnReferenceCountIsZero(v_rbp, v_r12, a3, a4);
    v_rbx = (*(unsigned __int64 *)(v_rbp + 40)) & (result);
    a1 = (v_rbx + v_rbx * 2) << (4);
    a1 = (a1) + (result);
    result = MiLockAndDecrementShareCount(a1, 2, a3, a4);
    result = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006D7070(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, void *Arg17)
{
    uint8_t *arg17 = (uint8_t *)Arg17;

    int64_t result;
    int64_t local_rbx;
    uint64_t v_stack_p20;

    result = (*(uint64_t *)(local_rbp + 0x18)) & (Arg1);
    *(uint64_t *)(local_rbp + 0x18) = result;
    result = MiGetPfnPriority(local_rbp, Arg2, Arg3, Arg4);
    Arg3 = 0;
    result = MiUpdatePfnPriority(Arg17, (uint32_t)((uint32_t)(result)), Arg3, Arg4);
    result = MiUnlockProtoPoolPage(local_r15, 18, Arg3, Arg4);
    result = MiMakePrototypePteDirect(v_stack_p20, 18, Arg3, Arg4);
    result = MiWriteRepurposedTransitionPte(local_rbp, result, Arg3, Arg4);
    result = (*(uint64_t *)(local_rbp + 0x18)) | (local_rbp);
    *(uint64_t *)(local_rbp + 0x18) = result;
    result = MiPfnReferenceCountIsZero(local_rbp, local_r12, Arg3, Arg4);
    local_rbx = (*(uint64_t *)(local_rbp + 0x28)) & (result);
    Arg1 = (local_rbx + local_rbx * 2) << (4);
    Arg1 = (Arg1) + (result);
    result = MiLockAndDecrementShareCount(Arg1, 2, Arg3, Arg4);
    result = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg17` | `+ 0x18` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D7070&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D7070[BB_006D7070]
```
