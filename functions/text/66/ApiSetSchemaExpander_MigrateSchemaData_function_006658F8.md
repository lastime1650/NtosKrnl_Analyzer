# ApiSetSchemaExpander_MigrateSchemaData

- RVA: `0x006658F8`–`0x00665A6F` (길이 `375` bytes)
- VA: `0x00000001406658F8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `108`개 명령, `375/375` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00665930` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0066595F` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0066598A` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x006659B5` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x006659E0` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00665A0B` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00665A36` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00665A59` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [ApiSetComposeSchema_V7](ApiSetComposeSchema_V7_function_00663CCC.md) at `0x00663E60`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006658F8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
006658FD  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00665902  57                              push rdi
00665903  48 83 EC 20                     sub rsp, 0x20
00665907  48 8B 79 08                     mov rdi, qword ptr [rcx + 8]
0066590B  48 8B D9                        mov rbx, rcx
0066590E  48 8B 71 20                     mov rsi, qword ptr [rcx + 0x20]
00665912  0F B7 47 12                     movzx eax, word ptr [rdi + 0x12]
00665916  8B 57 24                        mov edx, dword ptr [rdi + 0x24]
00665919  8B 4E 24                        mov ecx, dword ptr [rsi + 0x24]
0066591C  48 2B D0                        sub rdx, rax
0066591F  0F B7 46 12                     movzx eax, word ptr [rsi + 0x12]
00665923  48 03 D7                        add rdx, rdi
00665926  44 8B 47 28                     mov r8d, dword ptr [rdi + 0x28]
0066592A  48 2B C8                        sub rcx, rax
0066592D  48 03 CE                        add rcx, rsi
00665930  E8 0B 0F 06 00                  call 0x1406c6840
00665935  80 7B 10 00                     cmp byte ptr [rbx + 0x10], 0
00665939  74 29                           je 0x140665964
0066593B  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
0066593E  85 C0                           test eax, eax
00665940  74 22                           je 0x140665964
00665942  8B 57 18                        mov edx, dword ptr [rdi + 0x18]
00665945  44 8B C0                        mov r8d, eax
00665948  0F B7 47 12                     movzx eax, word ptr [rdi + 0x12]
0066594C  8B 4E 18                        mov ecx, dword ptr [rsi + 0x18]
0066594F  48 2B D0                        sub rdx, rax
00665952  0F B7 46 12                     movzx eax, word ptr [rsi + 0x12]
00665956  48 03 D7                        add rdx, rdi
00665959  48 2B C8                        sub rcx, rax
0066595C  48 03 CE                        add rcx, rsi
0066595F  E8 DC 0E 06 00                  call 0x1406c6840
00665964  0F B7 47 30                     movzx eax, word ptr [rdi + 0x30]
00665968  8B 57 2C                        mov edx, dword ptr [rdi + 0x2c]
0066596B  8B 4E 2C                        mov ecx, dword ptr [rsi + 0x2c]
0066596E  4C 8D 04 80                     lea r8, [rax + rax*4]
00665972  0F B7 47 12                     movzx eax, word ptr [rdi + 0x12]
00665976  48 2B D0                        sub rdx, rax
00665979  49 C1 E0 02                     shl r8, 2
0066597D  0F B7 46 12                     movzx eax, word ptr [rsi + 0x12]
00665981  48 03 D7                        add rdx, rdi
00665984  48 2B C8                        sub rcx, rax
00665987  48 03 CE                        add rcx, rsi
0066598A  E8 B1 0E 06 00                  call 0x1406c6840
0066598F  0F B7 47 3C                     movzx eax, word ptr [rdi + 0x3c]
00665993  8B 57 38                        mov edx, dword ptr [rdi + 0x38]
00665996  8B 4E 38                        mov ecx, dword ptr [rsi + 0x38]
00665999  4C 8D 04 80                     lea r8, [rax + rax*4]
0066599D  0F B7 47 12                     movzx eax, word ptr [rdi + 0x12]
006659A1  48 2B D0                        sub rdx, rax
006659A4  49 C1 E0 02                     shl r8, 2
006659A8  0F B7 46 12                     movzx eax, word ptr [rsi + 0x12]
006659AC  48 03 D7                        add rdx, rdi
006659AF  48 2B C8                        sub rcx, rax
006659B2  48 03 CE                        add rcx, rsi
006659B5  E8 86 0E 06 00                  call 0x1406c6840
006659BA  0F B7 47 48                     movzx eax, word ptr [rdi + 0x48]
006659BE  8B 57 44                        mov edx, dword ptr [rdi + 0x44]
006659C1  8B 4E 44                        mov ecx, dword ptr [rsi + 0x44]
006659C4  4C 8D 04 80                     lea r8, [rax + rax*4]
006659C8  0F B7 47 12                     movzx eax, word ptr [rdi + 0x12]
006659CC  48 2B D0                        sub rdx, rax
006659CF  49 C1 E0 02                     shl r8, 2
006659D3  0F B7 46 12                     movzx eax, word ptr [rsi + 0x12]
006659D7  48 03 D7                        add rdx, rdi
006659DA  48 2B C8                        sub rcx, rax
006659DD  48 03 CE                        add rcx, rsi
006659E0  E8 5B 0E 06 00                  call 0x1406c6840
006659E5  0F B7 47 60                     movzx eax, word ptr [rdi + 0x60]
006659E9  8B 57 5C                        mov edx, dword ptr [rdi + 0x5c]
006659EC  8B 4E 5C                        mov ecx, dword ptr [rsi + 0x5c]
006659EF  4C 8D 04 80                     lea r8, [rax + rax*4]
006659F3  0F B7 47 12                     movzx eax, word ptr [rdi + 0x12]
006659F7  48 2B D0                        sub rdx, rax
006659FA  49 C1 E0 02                     shl r8, 2
006659FE  0F B7 46 12                     movzx eax, word ptr [rsi + 0x12]
00665A02  48 03 D7                        add rdx, rdi
00665A05  48 2B C8                        sub rcx, rax
00665A08  48 03 CE                        add rcx, rsi
00665A0B  E8 30 0E 06 00                  call 0x1406c6840
00665A10  0F B7 47 54                     movzx eax, word ptr [rdi + 0x54]
00665A14  8B 57 50                        mov edx, dword ptr [rdi + 0x50]
00665A17  8B 4E 50                        mov ecx, dword ptr [rsi + 0x50]
00665A1A  4C 8D 04 40                     lea r8, [rax + rax*2]
00665A1E  0F B7 47 12                     movzx eax, word ptr [rdi + 0x12]
00665A22  48 2B D0                        sub rdx, rax
00665A25  49 C1 E0 02                     shl r8, 2
00665A29  0F B7 46 12                     movzx eax, word ptr [rsi + 0x12]
00665A2D  48 03 D7                        add rdx, rdi
00665A30  48 2B C8                        sub rcx, rax
00665A33  48 03 CE                        add rcx, rsi
00665A36  E8 05 0E 06 00                  call 0x1406c6840
00665A3B  0F B7 47 12                     movzx eax, word ptr [rdi + 0x12]
00665A3F  8B 57 68                        mov edx, dword ptr [rdi + 0x68]
00665A42  8B 4E 68                        mov ecx, dword ptr [rsi + 0x68]
00665A45  48 2B D0                        sub rdx, rax
00665A48  0F B7 46 12                     movzx eax, word ptr [rsi + 0x12]
00665A4C  48 03 D7                        add rdx, rdi
00665A4F  44 8B 47 6C                     mov r8d, dword ptr [rdi + 0x6c]
00665A53  48 2B C8                        sub rcx, rax
00665A56  48 03 CE                        add rcx, rsi
00665A59  E8 E2 0D 06 00                  call 0x1406c6840
00665A5E  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00665A63  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00665A68  48 83 C4 20                     add rsp, 0x20
00665A6C  5F                              pop rdi
00665A6D  C3                              ret
00665A6E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ApiSetSchemaExpander_MigrateSchemaData(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 36))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 18));
    a2 = (a2) + (*(unsigned __int64 *)(a1 + 8));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 36))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 32) + 18));
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 32));
    result = memcpy(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), a4);
    if ((*(unsigned __int8 *)(a1 + 16)) == 0) goto loc_00665964;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 28));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 28))) != 0) {
        a2 = *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 24);
        a3 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 28)));
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 18);
        a1 = *(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 24);
        a2 = (a2) - (result);
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 32) + 18);
        a2 = (a2) + (*(unsigned __int64 *)(a1 + 8));
        a1 = (a1) - (result);
        a1 = (a1) + (*(unsigned __int64 *)(a1 + 32));
        result = memcpy(a1, a2, a3, a4);
    }
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 44))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 18));
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 48) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 48) * 4) << (2);
    a2 = (a2) + (*(unsigned __int64 *)(a1 + 8));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 44))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 32) + 18));
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 32));
    result = memcpy(a1, a2, a3, a4);
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 56))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 18));
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 60) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 60) * 4) << (2);
    a2 = (a2) + (*(unsigned __int64 *)(a1 + 8));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 56))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 32) + 18));
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 32));
    result = memcpy(a1, a2, a3, a4);
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 68))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 18));
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 72) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 72) * 4) << (2);
    a2 = (a2) + (*(unsigned __int64 *)(a1 + 8));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 68))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 32) + 18));
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 32));
    result = memcpy(a1, a2, a3, a4);
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 92))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 18));
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 96) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 96) * 4) << (2);
    a2 = (a2) + (*(unsigned __int64 *)(a1 + 8));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 92))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 32) + 18));
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 32));
    result = memcpy(a1, a2, a3, a4);
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 80))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 18));
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 84) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 84) * 2) << (2);
    a2 = (a2) + (*(unsigned __int64 *)(a1 + 8));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 80))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 32) + 18));
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 32));
    result = memcpy(a1, a2, a3, a4);
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 104))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 18));
    a2 = (a2) + (*(unsigned __int64 *)(a1 + 8));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 104))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 32) + 18));
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 32));
    result = memcpy(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 108)), a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ApiSetSchemaExpander_MigrateSchemaData(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    a2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x24))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x12));
    a2 = (a2) + (*(uint64_t *)(arg1 + 0x8));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x24))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x20) + 0x12));
    Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x20));
    result = memcpy(Arg1, a2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28)), a4);
    if ((*(uint8_t *)(arg1 + 0x10)) == 0) goto loc_00665964;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x1C));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x1C))) != 0) {
        a2 = *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18);
        a3 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x1C)));
        result = *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x12);
        Arg1 = *(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x18);
        a2 = (a2) - (result);
        result = *(uint16_t *)(*(uint64_t *)(arg1 + 0x20) + 0x12);
        a2 = (a2) + (*(uint64_t *)(arg1 + 0x8));
        Arg1 = (Arg1) - (result);
        Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x20));
        result = memcpy(Arg1, a2, a3, a4);
    }
    a2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x2C))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x12));
    a3 = (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x30) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x30) * 4) << (2);
    a2 = (a2) + (*(uint64_t *)(arg1 + 0x8));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x2C))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x20) + 0x12));
    Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x20));
    result = memcpy(Arg1, a2, a3, a4);
    a2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x12));
    a3 = (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x3C) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x3C) * 4) << (2);
    a2 = (a2) + (*(uint64_t *)(arg1 + 0x8));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x38))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x20) + 0x12));
    Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x20));
    result = memcpy(Arg1, a2, a3, a4);
    a2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x44))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x12));
    a3 = (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x48) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x48) * 4) << (2);
    a2 = (a2) + (*(uint64_t *)(arg1 + 0x8));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x44))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x20) + 0x12));
    Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x20));
    result = memcpy(Arg1, a2, a3, a4);
    a2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x5C))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x12));
    a3 = (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x60) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x60) * 4) << (2);
    a2 = (a2) + (*(uint64_t *)(arg1 + 0x8));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x5C))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x20) + 0x12));
    Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x20));
    result = memcpy(Arg1, a2, a3, a4);
    a2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x50))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x12));
    a3 = (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x54) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x54) * 2) << (2);
    a2 = (a2) + (*(uint64_t *)(arg1 + 0x8));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x50))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x20) + 0x12));
    Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x20));
    result = memcpy(Arg1, a2, a3, a4);
    a2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x68))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x12));
    a2 = (a2) + (*(uint64_t *)(arg1 + 0x8));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x68))) - (*(uint16_t *)(*(uint64_t *)(arg1 + 0x20) + 0x12));
    Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x20));
    result = memcpy(Arg1, a2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x6C)), a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `8` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006658F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006658F8[BB_006658F8]
  bb_0066593B[BB_0066593B]
  bb_00665942[BB_00665942]
  bb_00665964[BB_00665964]
  bb_00665A6E[BB_00665A6E]
  bb_006658F8 -->|branch| bb_00665964
  bb_006658F8 -->|fallthrough| bb_0066593B
  bb_0066593B -->|branch| bb_00665964
  bb_0066593B -->|fallthrough| bb_00665942
  bb_00665942 -->|flow| bb_00665964
```
