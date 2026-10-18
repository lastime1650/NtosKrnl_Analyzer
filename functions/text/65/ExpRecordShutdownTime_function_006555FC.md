# ExpRecordShutdownTime

- RVA: `0x006555FC`–`0x006556D0` (길이 `212` bytes)
- VA: `0x00000001406555FC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C7C4C`
- 디코드: `49`개 명령, `212/212` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0065563F` → [RtlInitUnicodeString](../42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00655674` → [ZwOpenKey](../6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x00655688` → [RtlInitUnicodeString](../42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x006556AF` → [ZwSetValueKey](../6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x006556B8` → [ZwFlushKey](../6A/ZwFlushKey_function_006AEF10.md) (function, `0x006AEF10`)
- `0x006556C1` → [ZwClose](../6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [ExShutdownSystem](../../pagelk/B7/ExShutdownSystem_function_00B7290C.md) at `0x00B72931`

### Static image references
- `0x0065560D` → RVA `0x006CFFD0` (` ?? ::FNODOBFM::`string'`; read)
- `0x0065567D` → RVA `0x006CFFB0` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006555FC  40 55                           push rbp
006555FE  48 8B EC                        mov rbp, rsp
00655601  48 81 EC 80 00 00 00            sub rsp, 0x80
00655608  48 83 65 10 00                  and qword ptr [rbp + 0x10], 0
0065560D  48 8D 15 BC A9 07 00            lea rdx, [rip + 0x7a9bc]
00655614  33 C0                           xor eax, eax
00655616  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0065561A  21 45 EC                        and dword ptr [rbp - 0x14], eax
0065561D  0F 57 C0                        xorps xmm0, xmm0
00655620  89 45 D4                        mov dword ptr [rbp - 0x2c], eax
00655623  21 45 D4                        and dword ptr [rbp - 0x2c], eax
00655626  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
00655630  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00655634  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00655638  48 8B 00                        mov rax, qword ptr [rax]
0065563B  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0065563F  E8 3C 51 DD FF                  call 0x14042a780
00655644  48 83 65 D8 00                  and qword ptr [rbp - 0x28], 0
00655649  48 8D 45 B0                     lea rax, [rbp - 0x50]
0065564D  0F 57 C0                        xorps xmm0, xmm0
00655650  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00655654  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00655658  C7 45 D0 30 00 00 00            mov dword ptr [rbp - 0x30], 0x30
0065565F  BA 1F 00 02 00                  mov edx, 0x2001f
00655664  C7 45 E8 40 02 00 00            mov dword ptr [rbp - 0x18], 0x240
0065566B  48 8D 4D 10                     lea rcx, [rbp + 0x10]
0065566F  F3 0F 7F 45 F0                  movdqu xmmword ptr [rbp - 0x10], xmm0
00655674  E8 97 7C 05 00                  call 0x1406ad310
00655679  85 C0                           test eax, eax
0065567B  78 49                           js 0x1406556c6
0065567D  48 8D 15 2C A9 07 00            lea rdx, [rip + 0x7a92c]
00655684  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00655688  E8 F3 50 DD FF                  call 0x14042a780
0065568D  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00655691  48 8D 45 18                     lea rax, [rbp + 0x18]
00655695  C7 44 24 28 08 00 00 00         mov dword ptr [rsp + 0x28], 8
0065569D  48 8D 55 C0                     lea rdx, [rbp - 0x40]
006556A1  41 B9 03 00 00 00               mov r9d, 3
006556A7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006556AC  45 33 C0                        xor r8d, r8d
006556AF  E8 1C 86 05 00                  call 0x1406adcd0
006556B4  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
006556B8  E8 53 98 05 00                  call 0x1406aef10
006556BD  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
006556C1  E8 EA 7B 05 00                  call 0x1406ad2b0
006556C6  48 81 C4 80 00 00 00            add rsp, 0x80
006556CD  5D                              pop rbp
006556CE  C3                              ret
006556CF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpRecordShutdownTime(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m34;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (128);
    result = 0;
    v_stack_m34 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_p10 = *(unsigned __int64 *)(result);
    result = RtlInitUnicodeString(v_stack_m58, v_rip + 502204, a3, a4);
    v_stack_m28 = v_stack_m58;
    v_stack_m38 = 48;
    v_stack_m20 = 576;
    v_stack_m18 = v_xmm0;
    result = ZwOpenKey(v_stack_p8, (unsigned int)(0x2001FULL), v_stack_m38, a4);
    if (!(sign_flag)) {
        a2 = v_rip + 502060;
        a1 = v_stack_m48;
        result = RtlInitUnicodeString(a1, a2, v_stack_m38, a4);
        a1 = v_stack_p8;
        result = v_stack_p10;
        v_stack_m60 = 8;
        a2 = v_stack_m48;
        a4 = 3;
        v_stack_m68 = result;
        a3 = 0;
        result = ZwSetValueKey(a1, a2, a3, a4);
        a1 = v_stack_p8;
        result = ZwFlushKey(a1, a2, a3, a4);
        a1 = v_stack_p8;
        result = ZwClose(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
void ExpRecordShutdownTime(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m34;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (128);
    result = 0;
    v_stack_m34 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_p10 = *(uint64_t *)(result);
    result = RtlInitUnicodeString(v_stack_m58, v_rip + 502204, a3, a4);
    v_stack_m28 = v_stack_m58;
    v_stack_m38 = 48;
    v_stack_m20 = 576;
    v_stack_m18 = v_xmm0;
    result = ZwOpenKey(v_stack_p8, (uint32_t)(0x2001FULL), v_stack_m38, a4);
    if (!(sign_flag)) {
        a2 = v_rip + 502060;
        a1 = v_stack_m48;
        result = RtlInitUnicodeString(a1, a2, v_stack_m38, a4);
        a1 = v_stack_p8;
        result = v_stack_p10;
        v_stack_m60 = 8;
        a2 = v_stack_m48;
        a4 = 3;
        v_stack_m68 = result;
        a3 = 0;
        result = ZwSetValueKey(a1, a2, a3, a4);
        a1 = v_stack_p8;
        result = ZwFlushKey(a1, a2, a3, a4);
        a1 = v_stack_p8;
        result = ZwClose(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (128);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006555FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006555FC[BB_006555FC]
  bb_0065567D[BB_0065567D]
  bb_006556C6[BB_006556C6]
  bb_006556CF[BB_006556CF]
  bb_006555FC -->|branch| bb_006556C6
  bb_006555FC -->|fallthrough| bb_0065567D
  bb_0065567D -->|flow| bb_006556C6
```
