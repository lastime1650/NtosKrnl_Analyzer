# DifIoFreeControllerWrapper

- RVA: `0x0062A310`–`0x0062A460` (길이 `336` bytes)
- VA: `0x000000014062A310`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `90`개 명령, `336/336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062A338` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062A360` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062A38E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062A3B5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062A3CE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062A3D6` → [IoFreeController](../59/IoFreeController_function_005979F0.md) (function, `0x005979F0`)
- `0x0062A3FF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062A426` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062A43F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062A372` → RVA `0x00F048B8` (`.data`; read)
- `0x0062A37B` → RVA `0x00F04980` (`.data`; read)
- `0x0062A387` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062A310  48 8B C4                        mov rax, rsp
0062A313  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062A317  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062A31B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062A31F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062A323  41 56                           push r14
0062A325  48 83 EC 30                     sub rsp, 0x30
0062A329  48 8B E9                        mov rbp, rcx
0062A32C  0F 57 C0                        xorps xmm0, xmm0
0062A32F  B9 55 01 00 00                  mov ecx, 0x155
0062A334  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
0062A338  E8 F7 B6 E6 FF                  call 0x140495a34
0062A33D  48 8B F8                        mov rdi, rax
0062A340  48 85 C0                        test rax, rax
0062A343  0F 84 8A 00 00 00               je 0x14062a3d3
0062A349  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062A34C  A8 18                           test al, 0x18
0062A34E  74 0C                           je 0x14062a35c
0062A350  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0062A355  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062A35A  EB 0E                           jmp 0x14062a36a
0062A35C  A8 04                           test al, 4
0062A35E  74 0A                           je 0x14062a36a
0062A360  E8 A3 98 EA FF                  call 0x1404d3c08
0062A365  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062A36A  40 32 F6                        xor sil, sil
0062A36D  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0062A372  40 38 35 3F A5 8D 00            cmp byte ptr [rip + 0x8da53f], sil
0062A379  75 0C                           jne 0x14062a387
0062A37B  F7 05 FB A5 8D 00 00 08 00 00   test dword ptr [rip + 0x8da5fb], 0x800
0062A385  74 13                           je 0x14062a39a
0062A387  48 8D 0D F2 9A 8D 00            lea rcx, [rip + 0x8d9af2]
0062A38E  E8 8D C2 BE FF                  call 0x140216620
0062A393  40 8A F0                        mov sil, al
0062A396  84 C0                           test al, al
0062A398  74 39                           je 0x14062a3d3
0062A39A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0062A39E  49 8B 1E                        mov rbx, qword ptr [r14]
0062A3A1  EB 1A                           jmp 0x14062a3bd
0062A3A3  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062A3A7  48 85 C0                        test rax, rax
0062A3AA  74 0E                           je 0x14062a3ba
0062A3AC  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062A3B0  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062A3B5  E8 16 07 09 00                  call 0x1406baad0
0062A3BA  48 8B 1B                        mov rbx, qword ptr [rbx]
0062A3BD  49 3B DE                        cmp rbx, r14
0062A3C0  75 E1                           jne 0x14062a3a3
0062A3C2  40 84 F6                        test sil, sil
0062A3C5  74 0C                           je 0x14062a3d3
0062A3C7  48 8D 0D B2 9A 8D 00            lea rcx, [rip + 0x8d9ab2]
0062A3CE  E8 AD FA D1 FF                  call 0x140349e80
0062A3D3  48 8B CD                        mov rcx, rbp
0062A3D6  E8 15 D6 F6 FF                  call 0x1405979f0
0062A3DB  48 85 FF                        test rdi, rdi
0062A3DE  74 64                           je 0x14062a444
0062A3E0  40 32 F6                        xor sil, sil
0062A3E3  40 38 35 CE A4 8D 00            cmp byte ptr [rip + 0x8da4ce], sil
0062A3EA  75 0C                           jne 0x14062a3f8
0062A3EC  F7 05 8A A5 8D 00 00 08 00 00   test dword ptr [rip + 0x8da58a], 0x800
0062A3F6  74 13                           je 0x14062a40b
0062A3F8  48 8D 0D 81 9A 8D 00            lea rcx, [rip + 0x8d9a81]
0062A3FF  E8 1C C2 BE FF                  call 0x140216620
0062A404  40 8A F0                        mov sil, al
0062A407  84 C0                           test al, al
0062A409  74 39                           je 0x14062a444
0062A40B  48 83 C7 30                     add rdi, 0x30
0062A40F  48 8B 1F                        mov rbx, qword ptr [rdi]
0062A412  EB 1A                           jmp 0x14062a42e
0062A414  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062A418  48 85 C0                        test rax, rax
0062A41B  74 0E                           je 0x14062a42b
0062A41D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062A421  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062A426  E8 A5 06 09 00                  call 0x1406baad0
0062A42B  48 8B 1B                        mov rbx, qword ptr [rbx]
0062A42E  48 3B DF                        cmp rbx, rdi
0062A431  75 E1                           jne 0x14062a414
0062A433  40 84 F6                        test sil, sil
0062A436  74 0C                           je 0x14062a444
0062A438  48 8D 0D 41 9A 8D 00            lea rcx, [rip + 0x8d9a41]
0062A43F  E8 3C FA D1 FF                  call 0x140349e80
0062A444  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0062A449  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0062A44E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0062A453  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0062A458  48 83 C4 30                     add rsp, 0x30
0062A45C  41 5E                           pop r14
0062A45E  C3                              ret
0062A45F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoFreeControllerWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    result = DifGetAPIThunkContextById(341, a2, a3, a4);
    if (result == 0) goto loc_0062A3D3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062A35C;
    v_stack_m18 = v_stack_p0;
    goto loc_0062A36A;
loc_0062A35C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9282879)) != 0) goto loc_0062A387;
    if (((*(unsigned int *)(v_rip + 9283067)) & (0x800ULL)) == 0) goto loc_0062A39A;
loc_0062A387:
    result = ExAcquireRundownProtection(v_rip + 9280242, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062A3D3;
loc_0062A39A:
    goto loc_0062A3BD;
loc_0062A3A3:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062A3BD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062A3A3;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9280178;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoFreeController(a1, a2, a3, a4);
    if (result == 0) goto loc_0062A444;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9282766)) != 0) goto loc_0062A3F8;
    if (((*(unsigned int *)(v_rip + 9282954)) & (0x800ULL)) == 0) goto loc_0062A40B;
loc_0062A3F8:
    result = ExAcquireRundownProtection(v_rip + 9280129, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062A444;
loc_0062A40B:
    v_rdi = (result) + (48);
    goto loc_0062A42E;
loc_0062A414:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062A42E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_0062A414;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9280065;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoFreeControllerWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    result = DifGetAPIThunkContextById(341, a2, a3, a4);
    if (result == 0) goto loc_0062A3D3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062A35C;
    v_stack_m18 = v_stack_p0;
    goto loc_0062A36A;
loc_0062A35C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8DA53F)) != 0) goto loc_0062A387;
    if (((*(uint32_t *)(v_rip + 0x8DA5FB)) & (0x800ULL)) == 0) goto loc_0062A39A;
loc_0062A387:
    result = ExAcquireRundownProtection(v_rip + 9280242, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062A3D3;
loc_0062A39A:
    goto loc_0062A3BD;
loc_0062A3A3:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062A3BD:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062A3A3;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9280178;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = IoFreeController(Arg1, a2, a3, a4);
    if (result == 0) goto loc_0062A444;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8DA4CE)) != 0) goto loc_0062A3F8;
    if (((*(uint32_t *)(v_rip + 0x8DA58A)) & (0x800ULL)) == 0) goto loc_0062A40B;
loc_0062A3F8:
    result = ExAcquireRundownProtection(v_rip + 9280129, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062A444;
loc_0062A40B:
    local_rdi = (result) + (48);
    goto loc_0062A42E;
loc_0062A414:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062A42E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_0062A414;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9280065;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062A310&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062A310[BB_0062A310]
  bb_0062A349[BB_0062A349]
  bb_0062A350[BB_0062A350]
  bb_0062A35C[BB_0062A35C]
  bb_0062A360[BB_0062A360]
  bb_0062A36A[BB_0062A36A]
  bb_0062A37B[BB_0062A37B]
  bb_0062A387[BB_0062A387]
  bb_0062A39A[BB_0062A39A]
  bb_0062A3A3[BB_0062A3A3]
  bb_0062A3AC[BB_0062A3AC]
  bb_0062A3BA[BB_0062A3BA]
  bb_0062A3BD[BB_0062A3BD]
  bb_0062A3C2[BB_0062A3C2]
  bb_0062A3C7[BB_0062A3C7]
  bb_0062A3D3[BB_0062A3D3]
  bb_0062A3E0[BB_0062A3E0]
  bb_0062A3EC[BB_0062A3EC]
  bb_0062A3F8[BB_0062A3F8]
  bb_0062A40B[BB_0062A40B]
  bb_0062A414[BB_0062A414]
  bb_0062A41D[BB_0062A41D]
  bb_0062A42B[BB_0062A42B]
  bb_0062A42E[BB_0062A42E]
  bb_0062A433[BB_0062A433]
  bb_0062A438[BB_0062A438]
  bb_0062A444[BB_0062A444]
  bb_0062A45F[BB_0062A45F]
  bb_0062A310 -->|branch| bb_0062A3D3
  bb_0062A310 -->|fallthrough| bb_0062A349
  bb_0062A349 -->|branch| bb_0062A35C
  bb_0062A349 -->|fallthrough| bb_0062A350
  bb_0062A350 -->|branch| bb_0062A36A
  bb_0062A35C -->|branch| bb_0062A36A
  bb_0062A35C -->|fallthrough| bb_0062A360
  bb_0062A360 -->|flow| bb_0062A36A
  bb_0062A36A -->|branch| bb_0062A387
  bb_0062A36A -->|fallthrough| bb_0062A37B
  bb_0062A37B -->|branch| bb_0062A39A
  bb_0062A37B -->|fallthrough| bb_0062A387
  bb_0062A387 -->|branch| bb_0062A3D3
  bb_0062A387 -->|fallthrough| bb_0062A39A
  bb_0062A39A -->|branch| bb_0062A3BD
  bb_0062A3A3 -->|branch| bb_0062A3BA
  bb_0062A3A3 -->|fallthrough| bb_0062A3AC
  bb_0062A3AC -->|flow| bb_0062A3BA
  bb_0062A3BA -->|flow| bb_0062A3BD
  bb_0062A3BD -->|branch| bb_0062A3A3
  bb_0062A3BD -->|fallthrough| bb_0062A3C2
  bb_0062A3C2 -->|branch| bb_0062A3D3
  bb_0062A3C2 -->|fallthrough| bb_0062A3C7
  bb_0062A3C7 -->|flow| bb_0062A3D3
  bb_0062A3D3 -->|branch| bb_0062A444
  bb_0062A3D3 -->|fallthrough| bb_0062A3E0
  bb_0062A3E0 -->|branch| bb_0062A3F8
  bb_0062A3E0 -->|fallthrough| bb_0062A3EC
  bb_0062A3EC -->|branch| bb_0062A40B
  bb_0062A3EC -->|fallthrough| bb_0062A3F8
  bb_0062A3F8 -->|branch| bb_0062A444
  bb_0062A3F8 -->|fallthrough| bb_0062A40B
  bb_0062A40B -->|branch| bb_0062A42E
  bb_0062A414 -->|branch| bb_0062A42B
  bb_0062A414 -->|fallthrough| bb_0062A41D
  bb_0062A41D -->|flow| bb_0062A42B
  bb_0062A42B -->|flow| bb_0062A42E
  bb_0062A42E -->|branch| bb_0062A414
  bb_0062A42E -->|fallthrough| bb_0062A433
  bb_0062A433 -->|branch| bb_0062A444
  bb_0062A433 -->|fallthrough| bb_0062A438
  bb_0062A438 -->|flow| bb_0062A444
```
