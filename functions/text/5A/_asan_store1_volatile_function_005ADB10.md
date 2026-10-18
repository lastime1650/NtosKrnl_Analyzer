# _asan_store1_volatile

- RVA: `0x005ADB10`–`0x005ADBAF` (길이 `159` bytes)
- VA: `0x00000001405ADB10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E5F8`
- 디코드: `43`개 명령, `159/159` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005ADB7C` → [KasaniReport](KasaniReport_function_005AB0B0.md) (function, `0x005AB0B0`)
- `0x005ADB9E` → [KcsanValidateAddress](KcsanValidateAddress_function_005AF5E0.md) (function, `0x005AF5E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005ADB1A` → RVA `0x00FCEC6A` (`ALMOSTRO`; read)
- `0x005ADB3A` → RVA `0x00FC6ED8` (`ALMOSTRO`; read)
- `0x005ADB81` → RVA `0x00F8A7E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005ADB10  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005ADB15  57                              push rdi
005ADB16  48 83 EC 30                     sub rsp, 0x30
005ADB1A  80 3D 49 11 A2 00 00            cmp byte ptr [rip + 0xa21149], 0
005ADB21  48 8B D9                        mov rbx, rcx
005ADB24  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
005ADB29  74 78                           je 0x1405adba3
005ADB2B  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
005ADB35  48 3B C8                        cmp rcx, rax
005ADB38  72 69                           jb 0x1405adba3
005ADB3A  48 8B 05 97 93 A1 00            mov rax, qword ptr [rip + 0xa19397]
005ADB41  48 BA 00 00 00 00 00 80 00 00   movabs rdx, 0x800000000000
005ADB4B  48 03 D1                        add rdx, rcx
005ADB4E  48 C1 EA 03                     shr rdx, 3
005ADB52  0F B6 0C 02                     movzx ecx, byte ptr [rdx + rax]
005ADB56  84 C9                           test cl, cl
005ADB58  74 27                           je 0x1405adb81
005ADB5A  80 F9 08                        cmp cl, 8
005ADB5D  7D 22                           jge 0x1405adb81
005ADB5F  0F B6 C3                        movzx eax, bl
005ADB62  24 07                           and al, 7
005ADB64  FE C0                           inc al
005ADB66  3A C1                           cmp al, cl
005ADB68  7E 17                           jle 0x1405adb81
005ADB6A  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
005ADB6E  4C 8B CF                        mov r9, rdi
005ADB71  48 8B CB                        mov rcx, rbx
005ADB74  41 B0 01                        mov r8b, 1
005ADB77  BA 01 00 00 00                  mov edx, 1
005ADB7C  E8 2F D5 FF FF                  call 0x1405ab0b0
005ADB81  80 3D 60 CC 9D 00 00            cmp byte ptr [rip + 0x9dcc60], 0
005ADB88  74 19                           je 0x1405adba3
005ADB8A  41 B1 01                        mov r9b, 1
005ADB8D  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
005ADB92  45 0F B6 C1                     movzx r8d, r9b
005ADB96  BA 01 00 00 00                  mov edx, 1
005ADB9B  48 8B CB                        mov rcx, rbx
005ADB9E  E8 3D 1A 00 00                  call 0x1405af5e0
005ADBA3  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
005ADBA8  48 83 C4 30                     add rsp, 0x30
005ADBAC  5F                              pop rdi
005ADBAD  C3                              ret
005ADBAE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _asan_store1_volatile(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    if ((*(unsigned __int8 *)(v_rip + 10621257)) == 0) goto loc_005ADBA3;
    if (a1 < result) goto loc_005ADBA3;
    a2 = (a2) + (a1);
    a2 = (a2) >> (3);
    if ((unsigned __int8)(*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(v_rip + 10589079) * 1)) == 0) goto loc_005ADB81;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(v_rip + 10589079) * 1))) >= 8) goto loc_005ADB81;
    result = (unsigned __int8)(((unsigned __int8)(a1)) & (7));
    result = (unsigned __int8)((result) + 1);
    if (((unsigned __int8)(result)) >= = ((unsigned __int8)(*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(v_rip + 10589079) * 1)))) {
        v_stack_m18 = (unsigned __int8)(*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(v_rip + 10589079) * 1));
        a4 = v_stack_p0;
        a1 = a1;
        a3 = 1;
        a2 = 1;
        result = KasaniReport(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 10341472)) != 0) {
        a4 = 1;
        v_stack_m18 = v_stack_p0;
        a3 = (unsigned __int8)(a4);
        a2 = 1;
        a1 = a1;
        result = KcsanValidateAddress(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t _asan_store1_volatile(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    if ((*(uint8_t *)(v_rip + 0xA21149)) == 0) goto loc_005ADBA3;
    if (Arg1 < result) goto loc_005ADBA3;
    a2 = (a2) + (Arg1);
    a2 = (a2) >> (3);
    if ((uint8_t)(*(uint8_t *)(a2 + *(uint64_t *)(v_rip + 0xA19397) * 1)) == 0) goto loc_005ADB81;
    if (((uint8_t)(*(uint8_t *)(a2 + *(uint64_t *)(v_rip + 0xA19397) * 1))) >= 8) goto loc_005ADB81;
    result = (uint8_t)(((uint8_t)(Arg1)) & (7));
    result = (uint8_t)((result) + 1);
    if (((uint8_t)(result)) >= = ((uint8_t)(*(uint8_t *)(a2 + *(uint64_t *)(v_rip + 0xA19397) * 1)))) {
        v_stack_m18 = (uint8_t)(*(uint8_t *)(a2 + *(uint64_t *)(v_rip + 0xA19397) * 1));
        a4 = v_stack_p0;
        Arg1 = Arg1;
        a3 = 1;
        a2 = 1;
        result = KasaniReport(Arg1, a2, a3, a4);
    }
    if ((*(uint8_t *)(v_rip + 0x9DCC60)) != 0) {
        a4 = 1;
        v_stack_m18 = v_stack_p0;
        a3 = (uint8_t)(a4);
        a2 = 1;
        Arg1 = Arg1;
        result = KcsanValidateAddress(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005ADB10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005ADB10[BB_005ADB10]
  bb_005ADB2B[BB_005ADB2B]
  bb_005ADB3A[BB_005ADB3A]
  bb_005ADB5A[BB_005ADB5A]
  bb_005ADB5F[BB_005ADB5F]
  bb_005ADB6A[BB_005ADB6A]
  bb_005ADB81[BB_005ADB81]
  bb_005ADB8A[BB_005ADB8A]
  bb_005ADBA3[BB_005ADBA3]
  bb_005ADBAE[BB_005ADBAE]
  bb_005ADB10 -->|branch| bb_005ADBA3
  bb_005ADB10 -->|fallthrough| bb_005ADB2B
  bb_005ADB2B -->|branch| bb_005ADBA3
  bb_005ADB2B -->|fallthrough| bb_005ADB3A
  bb_005ADB3A -->|branch| bb_005ADB81
  bb_005ADB3A -->|fallthrough| bb_005ADB5A
  bb_005ADB5A -->|branch| bb_005ADB81
  bb_005ADB5A -->|fallthrough| bb_005ADB5F
  bb_005ADB5F -->|branch| bb_005ADB81
  bb_005ADB5F -->|fallthrough| bb_005ADB6A
  bb_005ADB6A -->|flow| bb_005ADB81
  bb_005ADB81 -->|branch| bb_005ADBA3
  bb_005ADB81 -->|fallthrough| bb_005ADB8A
  bb_005ADB8A -->|flow| bb_005ADBA3
```
