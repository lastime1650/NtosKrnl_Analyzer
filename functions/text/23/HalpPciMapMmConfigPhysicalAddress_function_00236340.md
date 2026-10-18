# HalpPciMapMmConfigPhysicalAddress

- RVA: `0x00236340`–`0x002363DD` (길이 `157` bytes)
- VA: `0x0000000140236340`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060858`
- 디코드: `34`개 명령, `157/157` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x002363CC` → [HalpMap](../3F/HalpMap_function_003F88F4.md) (function, `0x003F88F4`)

### Direct callers
- [sub_00235B5D](Unknown_function_00235B5D.md) at `0x00235C53`
- [HalpPciAccessMmConfigSpace](HalpPciAccessMmConfigSpace_function_0023683C.md) at `0x00236910`

### Static image references
- `0x00236344` → RVA `0x00F901E8` (`.data`; read)
- `0x002363D4` → RVA `0x00F901E8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00236340  48 83 EC 38                     sub rsp, 0x38
00236344  4C 8B 05 9D 9E D5 00            mov r8, qword ptr [rip + 0xd59e9d]
0023634B  4D 85 C0                        test r8, r8
0023634E  74 64                           je 0x1402363b4
00236350  49 8B C0                        mov rax, r8
00236353  48 BA FF FF FF FF 0F 00 00 00   movabs rdx, 0xfffffffff
0023635D  48 C1 E8 0C                     shr rax, 0xc
00236361  48 23 C2                        and rax, rdx
00236364  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
0023636E  48 8D 14 C2                     lea rdx, [rdx + rax*8]
00236372  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00236377  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0023637C  48 83 20 00                     and qword ptr [rax], 0
00236380  41 0F 01 38                     invlpg byte ptr [r8]
00236384  48 B8 00 F0 FF FF FF FF 0F 00   movabs rax, 0xffffffffff000
0023638E  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00236393  48 23 C8                        and rcx, rax
00236396  48 B8 1B 00 00 00 00 00 00 80   movabs rax, 0x800000000000001b
002363A0  48 0B C8                        or rcx, rax
002363A3  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002363A8  48 89 08                        mov qword ptr [rax], rcx
002363AB  49 8B C0                        mov rax, r8
002363AE  48 83 C4 38                     add rsp, 0x38
002363B2  C3                              ret
002363B3  CC                              int3
002363B4  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
002363BA  45 33 C0                        xor r8d, r8d
002363BD  41 B1 01                        mov r9b, 1
002363C0  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
002363C8  41 8D 50 01                     lea edx, [r8 + 1]
002363CC  E8 23 25 1C 00                  call 0x1403f88f4
002363D1  4C 8B C0                        mov r8, rax
002363D4  48 89 05 0D 9E D5 00            mov qword ptr [rip + 0xd59e0d], rax
002363DB  EB CE                           jmp 0x1402363ab
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpPciMapMmConfigPhysicalAddress(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;

    v_rsp = (v_rsp) - (56);
    if (*(unsigned __int64 *)(v_rip + 13999773) == 0) goto loc_002363B4;
    result = (*(unsigned __int64 *)(v_rip + 13999773)) >> (12);
    result = (result) & (a2);
    v_stack_p10 = a2 + result * 8;
    v_stack_p10 = a2 + result * 8;
    a1 = (a1) & (v_stack_p10);
    a1 = (a1) | (v_stack_p10);
    *(unsigned __int64 *)(v_stack_p10) = a1;
loc_002363AB:
    v_rsp = (v_rsp) + (56);
    return *(unsigned __int64 *)(v_rip + 13999773);
loc_002363B4:
    a3 = 0;
    v_stack_p20 = 4;
    result = HalpMap(a1, a3 + 1, a3, 1);
    *(unsigned __int64 *)(v_rip + 13999629) = result;
    goto loc_002363AB;
}
```

## 5. (Beta) C Style

```c
int64_t HalpPciMapMmConfigPhysicalAddress(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;

    local_rsp = (local_rsp) - (56);
    if (*(uint64_t *)(v_rip + 0xD59E9D) == 0) goto loc_002363B4;
    result = (*(uint64_t *)(v_rip + 0xD59E9D)) >> (12);
    result = (result) & (a2);
    v_stack_p10 = a2 + result * 8;
    v_stack_p10 = a2 + result * 8;
    Arg1 = (Arg1) & (v_stack_p10);
    Arg1 = (Arg1) | (v_stack_p10);
    *(uint64_t *)(v_stack_p10) = Arg1;
loc_002363AB:
    local_rsp = (local_rsp) + (56);
    return *(uint64_t *)(v_rip + 0xD59E9D);
loc_002363B4:
    a3 = 0;
    v_stack_p20 = 4;
    result = HalpMap(Arg1, a3 + 1, a3, 1);
    *(uint64_t *)(v_rip + 0xD59E0D) = result;
    goto loc_002363AB;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00236340&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00236340[BB_00236340]
  bb_00236350[BB_00236350]
  bb_002363AB[BB_002363AB]
  bb_002363B3[BB_002363B3]
  bb_002363B4[BB_002363B4]
  bb_00236340 -->|branch| bb_002363B4
  bb_00236340 -->|fallthrough| bb_00236350
  bb_00236350 -->|flow| bb_002363AB
  bb_002363B3 -->|flow| bb_002363B4
  bb_002363B4 -->|branch| bb_002363AB
```
