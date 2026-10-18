# IopEfiStatusToNTSTATUS

- RVA: `0x00721E30`–`0x00722000` (길이 `464` bytes)
- VA: `0x0000000140721E30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `148`개 명령, `464/464` bytes 표시
- 미해석 바이트: `12` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [IopEnumerateEnvironmentVariablesTrEE](IopEnumerateEnvironmentVariablesTrEE_function_007220A0.md) at `0x00722369`
- [IopEnumerateEnvironmentVariablesTrEE](IopEnumerateEnvironmentVariablesTrEE_function_007220A0.md) at `0x00722498`
- [IopGetEnvironmentVariableTrEE](IopGetEnvironmentVariableTrEE_function_007226B0.md) at `0x00722803`
- [IopQueryEnvironmentVariableInfoTrEE](IopQueryEnvironmentVariableInfoTrEE_function_00722AC0.md) at `0x00722B48`
- [IopSetEnvironmentVariableTrEE](IopSetEnvironmentVariableTrEE_function_00722CE0.md) at `0x00722DFE`

### Static image references
- `0x00721F7D` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00721FFE` → `0x00722000` (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00721E30  48 B8 0D 00 00 00 00 00 00 80   movabs rax, 0x800000000000000d
00721E3A  48 3B C8                        cmp rcx, rax
00721E3D  0F 87 27 01 00 00               ja 0x140721f6a
00721E43  0F 84 1A 01 00 00               je 0x140721f63
00721E49  48 B8 06 00 00 00 00 00 00 80   movabs rax, 0x8000000000000006
00721E53  48 3B C8                        cmp rcx, rax
00721E56  77 7F                           ja 0x140721ed7
00721E58  74 76                           je 0x140721ed0
00721E5A  48 85 C9                        test rcx, rcx
00721E5D  74 6D                           je 0x140721ecc
00721E5F  48 B8 01 00 00 00 00 00 00 80   movabs rax, 0x8000000000000001
00721E69  48 3B C8                        cmp rcx, rax
00721E6C  74 57                           je 0x140721ec5
00721E6E  48 B8 02 00 00 00 00 00 00 80   movabs rax, 0x8000000000000002
00721E78  48 3B C8                        cmp rcx, rax
00721E7B  74 41                           je 0x140721ebe
00721E7D  48 B8 03 00 00 00 00 00 00 80   movabs rax, 0x8000000000000003
00721E87  48 3B C8                        cmp rcx, rax
00721E8A  74 2B                           je 0x140721eb7
00721E8C  48 B8 04 00 00 00 00 00 00 80   movabs rax, 0x8000000000000004
00721E96  48 3B C8                        cmp rcx, rax
00721E99  74 15                           je 0x140721eb0
00721E9B  48 BA 05 00 00 00 00 00 00 80   movabs rdx, 0x8000000000000005
00721EA5  41 B8 23 00 00 C0               mov r8d, 0xc0000023
00721EAB  E9 82 00 00 00                  jmp 0x140721f32
00721EB0  B8 06 02 00 C0                  mov eax, 0xc0000206
00721EB5  C3                              ret
00721EB6  CC                              int3
00721EB7  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00721EBC  C3                              ret
00721EBD  CC                              int3
00721EBE  B8 0D 00 00 C0                  mov eax, 0xc000000d
00721EC3  C3                              ret
00721EC4  CC                              int3
00721EC5  B8 6C 02 00 C0                  mov eax, 0xc000026c
00721ECA  C3                              ret
00721ECB  CC                              int3
00721ECC  33 C0                           xor eax, eax
00721ECE  C3                              ret
00721ECF  CC                              int3
00721ED0  B8 25 02 00 C0                  mov eax, 0xc0000225
00721ED5  C3                              ret
00721ED6  CC                              int3
00721ED7  48 B8 07 00 00 00 00 00 00 80   movabs rax, 0x8000000000000007
00721EE1  48 3B C8                        cmp rcx, rax
00721EE4  74 76                           je 0x140721f5c
00721EE6  48 B8 08 00 00 00 00 00 00 80   movabs rax, 0x8000000000000008
00721EF0  48 3B C8                        cmp rcx, rax
00721EF3  74 60                           je 0x140721f55
00721EF5  48 B8 09 00 00 00 00 00 00 80   movabs rax, 0x8000000000000009
00721EFF  48 3B C8                        cmp rcx, rax
00721F02  74 4A                           je 0x140721f4e
00721F04  48 B8 0A 00 00 00 00 00 00 80   movabs rax, 0x800000000000000a
00721F0E  48 3B C8                        cmp rcx, rax
00721F11  74 34                           je 0x140721f47
00721F13  48 B8 0B 00 00 00 00 00 00 80   movabs rax, 0x800000000000000b
00721F1D  48 3B C8                        cmp rcx, rax
00721F20  74 1E                           je 0x140721f40
00721F22  48 BA 0C 00 00 00 00 00 00 80   movabs rdx, 0x800000000000000c
00721F2C  41 B8 78 01 00 C0               mov r8d, 0xc0000178
00721F32  48 3B CA                        cmp rcx, rdx
00721F35  B8 01 00 00 C0                  mov eax, 0xc0000001
00721F3A  41 0F 44 C0                     cmove eax, r8d
00721F3E  C3                              ret
00721F3F  CC                              int3
00721F40  B8 7F 00 00 C0                  mov eax, 0xc000007f
00721F45  C3                              ret
00721F46  CC                              int3
00721F47  B8 32 00 00 C0                  mov eax, 0xc0000032
00721F4C  C3                              ret
00721F4D  CC                              int3
00721F4E  B8 54 04 00 C0                  mov eax, 0xc0000454
00721F53  C3                              ret
00721F54  CC                              int3
00721F55  B8 A2 00 00 C0                  mov eax, 0xc00000a2
00721F5A  C3                              ret
00721F5B  CC                              int3
00721F5C  B8 85 01 00 C0                  mov eax, 0xc0000185
00721F61  C3                              ret
00721F62  CC                              int3
00721F63  B8 1C 00 00 80                  mov eax, 0x8000001c
00721F68  C3                              ret
00721F69  CC                              int3
00721F6A  48 B8 F2 FF FF FF FF FF FF 7F   movabs rax, 0x7ffffffffffffff2
00721F74  48 03 C1                        add rax, rcx
00721F77  48 83 F8 0C                     cmp rax, 0xc
00721F7B  77 48                           ja 0x140721fc5
00721F7D  48 8D 0D 7C E0 8D FF            lea rcx, [rip - 0x721f84]
00721F84  8B 84 81 CC 1F 72 00            mov eax, dword ptr [rcx + rax*4 + 0x721fcc]
00721F8B  48 03 C1                        add rax, rcx
00721F8E  FF E0                           jmp rax
00721F90  CC                              int3
00721F91  CC                              int3
00721F92  CC                              int3
00721F93  CC                              int3
00721F94  B8 00 01 00 C0                  mov eax, 0xc0000100
00721F99  C3                              ret
00721F9A  CC                              int3
00721F9B  B8 22 00 00 C0                  mov eax, 0xc0000022
00721FA0  C3                              ret
00721FA1  CC                              int3
00721FA2  B8 72 02 00 C0                  mov eax, 0xc0000272
00721FA7  C3                              ret
00721FA8  CC                              int3
00721FA9  B8 02 01 00 00                  mov eax, 0x102
00721FAE  C3                              ret
00721FAF  CC                              int3
00721FB0  B8 A3 00 00 C0                  mov eax, 0xc00000a3
00721FB5  C3                              ret
00721FB6  CC                              int3
00721FB7  B8 38 00 00 C0                  mov eax, 0xc0000038
00721FBC  C3                              ret
00721FBD  CC                              int3
00721FBE  B8 40 02 00 C0                  mov eax, 0xc0000240
00721FC3  C3                              ret
00721FC4  CC                              int3
00721FC5  B8 01 00 00 C0                  mov eax, 0xc0000001
00721FCA  C3                              ret
00721FCB  CC                              int3
00721FCC  94                              xchg esp, eax
00721FCD  1F                              .byte 0x1f
00721FCE  72 00                           jb 0x140721fd0
00721FD0  9B                              wait
00721FD1  1F                              .byte 0x1f
00721FD2  72 00                           jb 0x140721fd4
00721FD4  A9 1F 72 00 A2                  test eax, 0xa200721f
00721FD9  1F                              .byte 0x1f
00721FDA  72 00                           jb 0x140721fdc
00721FDC  A9 1F 72 00 B0                  test eax, 0xb000721f
00721FE1  1F                              .byte 0x1f
00721FE2  72 00                           jb 0x140721fe4
00721FE4  B7 1F                           mov bh, 0x1f
00721FE6  72 00                           jb 0x140721fe8
00721FE8  BE 1F 72 00 C5                  mov esi, 0xc500721f
00721FED  1F                              .byte 0x1f
00721FEE  72 00                           jb 0x140721ff0
00721FF0  C5                              .byte 0xc5
00721FF1  1F                              .byte 0x1f
00721FF2  72 00                           jb 0x140721ff4
00721FF4  C5                              .byte 0xc5
00721FF5  1F                              .byte 0x1f
00721FF6  72 00                           jb 0x140721ff8
00721FF8  C5                              .byte 0xc5
00721FF9  1F                              .byte 0x1f
00721FFA  72 00                           jb 0x140721ffc
00721FFC  9B                              wait
00721FFD  1F                              .byte 0x1f
00721FFE  72 00                           jb 0x140722000
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopEfiStatusToNTSTATUS(__int64 a1)
{
    __int64 result;

    if (a1 > result) goto loc_00721F6A;
    if (a1 == result) goto loc_00721F63;
    if (a1 > result) goto loc_00721ED7;
    if (a1 == result) goto loc_00721ED0;
    if (a1 == 0) goto loc_00721ECC;
    if (a1 == result) goto loc_00721EC5;
    if (a1 == result) goto loc_00721EBE;
    if (a1 == result) goto loc_00721EB7;
    if (a1 == result) goto loc_00721EB0;
    goto loc_00721F32;
loc_00721EB0:
    return (unsigned int)(0xC0000206ULL);
loc_00721EB7:
    return (unsigned int)(0xC00000BBULL);
loc_00721EBE:
    return (unsigned int)(0xC000000DULL);
loc_00721EC5:
    return (unsigned int)(0xC000026CULL);
loc_00721ECC:
    result = 0;
    return result;
loc_00721ED0:
    return (unsigned int)(0xC0000225ULL);
loc_00721ED7:
    if (a1 == ((unsigned int)(0xC0000225ULL))) goto loc_00721F5C;
    if (a1 == ((unsigned int)(0xC0000225ULL))) goto loc_00721F55;
    if (a1 == ((unsigned int)(0xC0000225ULL))) goto loc_00721F4E;
    if (a1 == ((unsigned int)(0xC0000225ULL))) goto loc_00721F47;
    if (a1 == ((unsigned int)(0xC0000225ULL))) goto loc_00721F40;
loc_00721F32:
    result = (unsigned int)(0xC0000001ULL);
    if (a1 == a2) { result = (unsigned int)((unsigned int)(0xC0000178ULL)); }
    return result;
loc_00721F40:
    return (unsigned int)(0xC000007FULL);
loc_00721F47:
    return (unsigned int)(0xC0000032ULL);
loc_00721F4E:
    return (unsigned int)(0xC0000454ULL);
loc_00721F55:
    return (unsigned int)(0xC00000A2ULL);
loc_00721F5C:
    return (unsigned int)(0xC0000185ULL);
loc_00721F63:
    return (unsigned int)(0x8000001CULL);
loc_00721F6A:
    result = ((unsigned int)(0x8000001CULL)) + (a1);
    if (result > 12) goto loc_00721FC5;
    result = ((unsigned int)(*(unsigned int *)(v_rip - 7479172 + result * 4 + 7479244))) + (v_rip - 7479172);
loc_00721FC5:
    return (unsigned int)(0xC0000001ULL);
}
```

## 5. (Beta) C Style

```c
int64_t IopEfiStatusToNTSTATUS(int64_t Arg1)
{
    int64_t result;

    if (Arg1 > result) goto loc_00721F6A;
    if (Arg1 == result) goto loc_00721F63;
    if (Arg1 > result) goto loc_00721ED7;
    if (Arg1 == result) goto loc_00721ED0;
    if (Arg1 == 0) goto loc_00721ECC;
    if (Arg1 == result) goto loc_00721EC5;
    if (Arg1 == result) goto loc_00721EBE;
    if (Arg1 == result) goto loc_00721EB7;
    if (Arg1 == result) goto loc_00721EB0;
    goto loc_00721F32;
loc_00721EB0:
    return (uint32_t)(0xC0000206ULL);
loc_00721EB7:
    return (uint32_t)(0xC00000BBULL);
loc_00721EBE:
    return (uint32_t)(0xC000000DULL);
loc_00721EC5:
    return (uint32_t)(0xC000026CULL);
loc_00721ECC:
    result = 0;
    return result;
loc_00721ED0:
    return (uint32_t)(0xC0000225ULL);
loc_00721ED7:
    if (Arg1 == ((uint32_t)(0xC0000225ULL))) goto loc_00721F5C;
    if (Arg1 == ((uint32_t)(0xC0000225ULL))) goto loc_00721F55;
    if (Arg1 == ((uint32_t)(0xC0000225ULL))) goto loc_00721F4E;
    if (Arg1 == ((uint32_t)(0xC0000225ULL))) goto loc_00721F47;
    if (Arg1 == ((uint32_t)(0xC0000225ULL))) goto loc_00721F40;
loc_00721F32:
    result = (uint32_t)(0xC0000001ULL);
    if (Arg1 == a2) { result = (uint32_t)((uint32_t)(0xC0000178ULL)); }
    return result;
loc_00721F40:
    return (uint32_t)(0xC000007FULL);
loc_00721F47:
    return (uint32_t)(0xC0000032ULL);
loc_00721F4E:
    return (uint32_t)(0xC0000454ULL);
loc_00721F55:
    return (uint32_t)(0xC00000A2ULL);
loc_00721F5C:
    return (uint32_t)(0xC0000185ULL);
loc_00721F63:
    return (uint32_t)(0x8000001CULL);
loc_00721F6A:
    result = ((uint32_t)(0x8000001CULL)) + (Arg1);
    if (result > 12) goto loc_00721FC5;
    result = ((uint32_t)(*(uint32_t *)(v_rip - 0x721F84 + result * 4 + 0x721FCC))) + (v_rip - 7479172);
loc_00721FC5:
    return (uint32_t)(0xC0000001ULL);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00721E30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
