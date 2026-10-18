# ExpLicenseWatchInitWorker

- RVA: `0x00C6CEE0`–`0x00C6CFA0` (길이 `192` bytes)
- VA: `0x0000000140C6CEE0`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E5F8`
- 디코드: `52`개 명령, `192/192` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00C6CF17` → [HvlQueryVsmConnection](../../text/45/HvlQueryVsmConnection_function_0045D180.md) (function, `0x0045D180`)
- `0x00C6CF6B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C6CF8E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [ExpWatchProductTypeInitialization](../C5/ExpWatchProductTypeInitialization_function_00C52170.md) at `0x00C5236A`

### Static image references
- `0x00C6CEED` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x00C6CF22` → RVA `0x00FC41C4` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00C6CF17` → [HvlQueryVsmConnection](../../text/45/HvlQueryVsmConnection_function_0045D180.md) (`INIT` → `.text`)
  - `0x00C6CF6B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C6CF8E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C6CEE0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C6CEE5  57                              push rdi
00C6CEE6  48 83 EC 30                     sub rsp, 0x30
00C6CEEA  0F AE E8                        lfence
00C6CEED  48 8B 05 4C BD 35 00            mov rax, qword ptr [rip + 0x35bd4c]
00C6CEF4  33 C9                           xor ecx, ecx
00C6CEF6  48 8B 58 78                     mov rbx, qword ptr [rax + 0x78]
00C6CEFA  48 8B 78 70                     mov rdi, qword ptr [rax + 0x70]
00C6CEFE  48 83 60 78 00                  and qword ptr [rax + 0x78], 0
00C6CF03  48 83 60 70 00                  and qword ptr [rax + 0x70], 0
00C6CF08  A0 D4 02 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff780000002d4]
00C6CF11  44 8A D8                        mov r11b, al
00C6CF14  41 D0 EB                        shr r11b, 1
00C6CF17  E8 64 02 7F FF                  call 0x14045d180
00C6CF1C  84 C0                           test al, al
00C6CF1E  41 0F 94 C2                     sete r10b
00C6CF22  39 0D 9C 72 35 00               cmp dword ptr [rip + 0x35729c], ecx
00C6CF28  41 0F 95 C0                     setne r8b
00C6CF2C  0F 31                           rdtsc
00C6CF2E  48 C1 E2 20                     shl rdx, 0x20
00C6CF32  45 22 D0                        and r10b, r8b
00C6CF35  48 0B C2                        or rax, rdx
00C6CF38  44 8D 41 01                     lea r8d, [rcx + 1]
00C6CF3C  4C 8B C8                        mov r9, rax
00C6CF3F  B8 1F 85 EB 51                  mov eax, 0x51eb851f
00C6CF44  49 C1 E9 03                     shr r9, 3
00C6CF48  41 F7 E1                        mul r9d
00C6CF4B  C1 EA 05                        shr edx, 5
00C6CF4E  6B C2 64                        imul eax, edx, 0x64
00C6CF51  41 0F B6 D2                     movzx edx, r10b
00C6CF55  44 2B C8                        sub r9d, eax
00C6CF58  41 83 F9 03                     cmp r9d, 3
00C6CF5C  44 0F 46 C2                     cmovbe r8d, edx
00C6CF60  45 0A C3                        or r8b, r11b
00C6CF63  75 2F                           jne 0x140c6cf94
00C6CF65  48 8B CB                        mov rcx, rbx
00C6CF68  48 8B C7                        mov rax, rdi
00C6CF6B  E8 60 DB A4 FF                  call 0x1406baad0
00C6CF70  83 F8 01                        cmp eax, 1
00C6CF73  74 1F                           je 0x140c6cf94
00C6CF75  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00C6CF7B  45 33 C9                        xor r9d, r9d
00C6CF7E  BA 42 42 42 42                  mov edx, 0x42424242
00C6CF83  B9 9A 00 00 00                  mov ecx, 0x9a
00C6CF88  41 B8 6A 02 00 C0               mov r8d, 0xc000026a
00C6CF8E  E8 CD 06 89 FF                  call 0x1404fd660
00C6CF93  CC                              int3
00C6CF94  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00C6CF99  48 83 C4 30                     add rsp, 0x30
00C6CF9D  5F                              pop rdi
00C6CF9E  C3                              ret
00C6CF9F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpLicenseWatchInitWorker(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    a1 = 0;
    v_r11 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_rip + 3521868))) >> (1));
    result = HvlQueryVsmConnection(a1, a2, a3, a4);
    v_r10 = ((unsigned __int8)(result) == 0) ? 1 : 0;
    a3 = ((*(unsigned int *)(v_rip + 3502748)) != 0) ? 1 : 0;
    a2 = (a2) << (32);
    v_r10 = (unsigned __int8)((v_r10) & ((unsigned __int8)(a3)));
    result = (result) | (a2);
    a4 = (result) >> (3);
    a2 = (unsigned int)((a2) >> (5));
    result = (unsigned int)(((unsigned int)(0x51EB851FULL)) * ((unsigned int)(a2)));
    a4 = (unsigned int)((a4) - ((unsigned int)(result)));
    a3 = a1 + 1;
    if (((unsigned int)(a4)) <= 3) { a3 = (unsigned int)((unsigned __int8)(v_r10)); }
    a3 = (unsigned __int8)((a3) | ((unsigned __int8)(v_r11)));
    if (condition_is_not_equal) goto loc_00C6CF94;
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3521868) + 120), (unsigned __int8)(v_r10), a3, a4);
    if (((unsigned int)(result)) != 1) {
        a4 = 0;
        a2 = 0x42424242ULL;
        a1 = 154;
        a3 = 0xC000026AULL;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpLicenseWatchInitWorker(int32_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    Arg1 = 0;
    local_r11 = (uint8_t)(((uint8_t)(*(uint64_t *)(v_rip + 0x35BD4C))) >> (1));
    result = HvlQueryVsmConnection(Arg1, Arg2, a3, a4);
    local_r10 = ((uint8_t)(result) == 0) ? 1 : 0;
    a3 = ((*(uint32_t *)(v_rip + 0x35729C)) != 0) ? 1 : 0;
    Arg2 = (Arg2) << (32);
    local_r10 = (uint8_t)((local_r10) & ((uint8_t)(a3)));
    result = (result) | (Arg2);
    a4 = (result) >> (3);
    Arg2 = (uint32_t)((Arg2) >> (5));
    result = (uint32_t)(((uint32_t)(0x51EB851FULL)) * ((uint32_t)(Arg2)));
    a4 = (uint32_t)((a4) - ((uint32_t)(result)));
    a3 = Arg1 + 1;
    if (((uint32_t)(a4)) <= 3) { a3 = (uint32_t)((uint8_t)(local_r10)); }
    a3 = (uint8_t)((a3) | ((uint8_t)(local_r11)));
    if (condition_is_not_equal) goto loc_00C6CF94;
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(v_rip + 0x35BD4C) + 0x78), (uint8_t)(local_r10), a3, a4);
    if (((uint32_t)(result)) != 1) {
        a4 = 0;
        Arg2 = 0x42424242ULL;
        Arg1 = 154;
        a3 = 0xC000026AULL;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C6CEE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C6CEE0[BB_00C6CEE0]
  bb_00C6CF65[BB_00C6CF65]
  bb_00C6CF75[BB_00C6CF75]
  bb_00C6CF94[BB_00C6CF94]
  bb_00C6CF9F[BB_00C6CF9F]
  bb_00C6CEE0 -->|branch| bb_00C6CF94
  bb_00C6CEE0 -->|fallthrough| bb_00C6CF65
  bb_00C6CF65 -->|branch| bb_00C6CF94
  bb_00C6CF65 -->|fallthrough| bb_00C6CF75
  bb_00C6CF75 -->|flow| bb_00C6CF94
```
