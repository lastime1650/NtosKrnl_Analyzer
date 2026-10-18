# VmpLogTbFlushSlatFlushEntire

- RVA: `0x0064DD64`–`0x0064DE32` (길이 `206` bytes)
- VA: `0x000000014064DD64`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AA6F8`
- 디코드: `40`개 명령, `206/206` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064DD99` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0064DE14` → [tlgWriteEx_EtwWriteEx](../4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (function, `0x004AA348`)
- `0x0064DE24` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [VmpFlushTb](../31/VmpFlushTb_function_00311BD0.md) at `0x00311F4D`
- [sub_00314756](../31/Unknown_function_00314756.md) at `0x00314775`

### Static image references
- `0x0064DD6B` → RVA `0x00E0A740` (`.data`; read)
- `0x0064DD7D` → RVA `0x00F02458` (`.data`; read)
- `0x0064DDAB` → RVA `0x000537A3` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064DD64  48 81 EC A8 00 00 00            sub rsp, 0xa8
0064DD6B  48 8B 05 CE C9 7B 00            mov rax, qword ptr [rip + 0x7bc9ce]
0064DD72  48 33 C4                        xor rax, rsp
0064DD75  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0064DD7D  4C 8B 05 D4 46 8B 00            mov r8, qword ptr [rip + 0x8b46d4]
0064DD84  4C 8B CA                        mov r9, rdx
0064DD87  41 83 38 05                     cmp dword ptr [r8], 5
0064DD8B  0F 86 88 00 00 00               jbe 0x14064de19
0064DD91  BA 00 01 00 00                  mov edx, 0x100
0064DD96  49 8B C8                        mov rcx, r8
0064DD99  E8 02 0D DE FF                  call 0x14042eaa0
0064DD9E  84 C0                           test al, al
0064DDA0  74 77                           je 0x14064de19
0064DDA2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0064DDAB  48 8D 15 F1 59 A0 FF            lea rdx, [rip - 0x5fa60f]
0064DDB2  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0064DDB9  8B 81 D0 01 00 00               mov eax, dword ptr [rcx + 0x1d0]
0064DDBF  B9 04 00 00 00                  mov ecx, 4
0064DDC4  83 64 24 7C 00                  and dword ptr [rsp + 0x7c], 0
0064DDC9  83 A4 24 8C 00 00 00 00         and dword ptr [rsp + 0x8c], 0
0064DDD1  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0064DDD5  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0064DDDA  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0064DDDF  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0064DDE4  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0064DDEC  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0064DDF1  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0064DDF6  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0064DDFA  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
0064DDFE  49 8B C8                        mov rcx, r8
0064DE01  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
0064DE06  45 33 C9                        xor r9d, r9d
0064DE09  C7 84 24 88 00 00 00 08 00 00 00  mov dword ptr [rsp + 0x88], 8
0064DE14  E8 2F C5 E5 FF                  call 0x1404aa348
0064DE19  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0064DE21  48 33 CC                        xor rcx, rsp
0064DE24  E8 17 E8 05 00                  call 0x1406ac640
0064DE29  48 81 C4 A8 00 00 00            add rsp, 0xa8
0064DE30  C3                              ret
0064DE31  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmpLogTbFlushSlatFlushEntire(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;

    v_rsp = (v_rsp) - (168);
    result = (*(unsigned __int64 *)(v_rip + 8112590)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9127636))) <= 5) goto loc_0064DE19;
    result = tlgKeywordOn(*(unsigned __int64 *)(v_rip + 9127636), 256, *(unsigned __int64 *)(v_rip + 9127636), a2);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = v_rip - 6268431;
        a1 = *(unsigned __int64 *)(result + 184);
        result = *(unsigned int *)(a1 + 464);
        a1 = 4;
        v_stack_m68 = (unsigned int)(result);
        result = v_stack_m68;
        v_stack_m38 = result;
        result = v_stack_m60;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m70 = result;
        v_stack_m78 = (unsigned int)(a1);
        v_stack_m30 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 9127636);
        v_stack_m60 = a2;
        a4 = 0;
        v_stack_m20 = 8;
        result = tlgWriteEx_EtwWriteEx(a1, a2, *(unsigned __int64 *)(v_rip + 9127636), a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, *(unsigned __int64 *)(v_rip + 9127636), a4);
    v_rsp = (v_rsp) + (168);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VmpLogTbFlushSlatFlushEntire(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;

    local_rsp = (local_rsp) - (168);
    result = (*(uint64_t *)(v_rip + 0x7BC9CE)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x8B46D4))) <= 5) goto loc_0064DE19;
    result = tlgKeywordOn(*(uint64_t *)(v_rip + 0x8B46D4), 256, *(uint64_t *)(v_rip + 0x8B46D4), Arg2);
    if ((uint8_t)(result) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = v_rip - 6268431;
        Arg1 = *(uint64_t *)(result + 0xB8);
        result = *(uint32_t *)(Arg1 + 0x1D0);
        Arg1 = 4;
        v_stack_m68 = (uint32_t)(result);
        result = v_stack_m68;
        v_stack_m38 = result;
        result = v_stack_m60;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m70 = result;
        v_stack_m78 = (uint32_t)(Arg1);
        v_stack_m30 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x8B46D4);
        v_stack_m60 = Arg2;
        a4 = 0;
        v_stack_m20 = 8;
        result = tlgWriteEx_EtwWriteEx(Arg1, Arg2, *(uint64_t *)(v_rip + 0x8B46D4), a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, *(uint64_t *)(v_rip + 0x8B46D4), a4);
    local_rsp = (local_rsp) + (168);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064DD64&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064DD64[BB_0064DD64]
  bb_0064DD91[BB_0064DD91]
  bb_0064DDA2[BB_0064DDA2]
  bb_0064DE19[BB_0064DE19]
  bb_0064DE31[BB_0064DE31]
  bb_0064DD64 -->|branch| bb_0064DE19
  bb_0064DD64 -->|fallthrough| bb_0064DD91
  bb_0064DD91 -->|branch| bb_0064DE19
  bb_0064DD91 -->|fallthrough| bb_0064DDA2
  bb_0064DDA2 -->|flow| bb_0064DE19
```
