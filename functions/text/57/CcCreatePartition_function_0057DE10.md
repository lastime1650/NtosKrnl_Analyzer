# CcCreatePartition

- RVA: `0x0057DE10`–`0x0057DE96` (길이 `134` bytes)
- VA: `0x000000014057DE10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `34`개 명령, `134/134` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0057DE45` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x0057DE5A` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x0057DE6D` → [CcInitializePartition](CcInitializePartition_function_0057E4D8.md) (function, `0x0057E4D8`)
- `0x0057DE80` → [CcDeletePartition](CcDeletePartition_function_0057DE9C.md) (function, `0x0057DE9C`)

### Direct callers
- [sub_006E8790](../6E/Unknown_function_006E8790.md) at `0x006E8790`
- [CcInitializeCacheManager](../../init/BE/CcInitializeCacheManager_function_00BEE2E8.md) at `0x00BEE3E7`

### Static image references
- `0x0057DE1A` → RVA `0x00E65B88` (`.data`; read)
- `0x0057DE21` → RVA `0x006C8DA0` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057DE2D` → RVA `0x006C8D90` (` ?? ::FNODOBFM::`string'`; read)
- `0x0057DE37` → RVA `0x006C8D10` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0057DE5A` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0057DE10  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0057DE15  57                              push rdi
0057DE16  48 83 EC 20                     sub rsp, 0x20
0057DE1A  80 3D 67 7D 8E 00 00            cmp byte ptr [rip + 0x8e7d67], 0
0057DE21  48 8D 05 78 AF 14 00            lea rax, [rip + 0x14af78]
0057DE28  BA 02 00 00 00                  mov edx, 2
0057DE2D  4C 8D 0D 5C AF 14 00            lea r9, [rip + 0x14af5c]
0057DE34  48 8B F9                        mov rdi, rcx
0057DE37  4C 8D 05 D2 AE 14 00            lea r8, [rip + 0x14aed2]
0057DE3E  4C 0F 44 C8                     cmove r9, rax
0057DE42  8D 4A 7D                        lea ecx, [rdx + 0x7d]
0057DE45  E8 46 B4 DD FF                  call 0x140359290
0057DE4A  BA 40 06 00 00                  mov edx, 0x640
0057DE4F  B9 00 02 00 00                  mov ecx, 0x200
0057DE54  41 B8 43 63 50 72               mov r8d, 0x72506343
0057DE5A  E8 B1 41 60 00                  call 0x140b82010
0057DE5F  48 8B D8                        mov rbx, rax
0057DE62  48 85 C0                        test rax, rax
0057DE65  74 20                           je 0x14057de87
0057DE67  48 8B D7                        mov rdx, rdi
0057DE6A  48 8B C8                        mov rcx, rax
0057DE6D  E8 66 06 00 00                  call 0x14057e4d8
0057DE72  84 C0                           test al, al
0057DE74  75 11                           jne 0x14057de87
0057DE76  48 8B CB                        mov rcx, rbx
0057DE79  C6 83 0E 05 00 00 02            mov byte ptr [rbx + 0x50e], 2
0057DE80  E8 17 00 00 00                  call 0x14057de9c
0057DE85  33 DB                           xor ebx, ebx
0057DE87  48 8B C3                        mov rax, rbx
0057DE8A  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0057DE8F  48 83 C4 20                     add rsp, 0x20
0057DE93  5F                              pop rdi
0057DE94  C3                              ret
0057DE95  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcCreatePartition(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a4 = v_rip + 1355612;
    if ((*(unsigned __int8 *)(v_rip + 9338215)) == 0) { a4 = v_rip + 1355640; }
    result = DbgPrintEx(2 + 125, 2, v_rip + 1355474, a4);
    result = ExAllocatePoolWithTag(512, (unsigned int)(0x640ULL), (unsigned int)(0x72506343ULL), a4);
    if (result == 0) goto loc_0057DE87;
    result = CcInitializePartition(result, a1, (unsigned int)(0x72506343ULL), a4);
    v_rbx = result;
    if ((unsigned __int8)(result) == 0) {
        a1 = result;
        *(unsigned __int8 *)(result + 1294) = 2;
        result = CcDeletePartition(a1, a1, (unsigned int)(0x72506343ULL), a4);
        v_rbx = 0;
    }
    v_rsp = (v_rsp) + (32);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t CcCreatePartition(int64_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    a4 = v_rip + 1355612;
    if ((*(uint8_t *)(v_rip + 0x8E7D67)) == 0) { a4 = v_rip + 1355640; }
    result = DbgPrintEx(2 + 125, 2, v_rip + 1355474, a4);
    result = ExAllocatePoolWithTag(512, (uint32_t)(0x640ULL), (uint32_t)(0x72506343ULL), a4);
    if (result == 0) goto loc_0057DE87;
    result = CcInitializePartition(result, Arg1, (uint32_t)(0x72506343ULL), a4);
    local_rbx = result;
    if ((uint8_t)(result) == 0) {
        Arg1 = result;
        *(uint8_t *)(result + 0x50E) = 2;
        result = CcDeletePartition(Arg1, Arg1, (uint32_t)(0x72506343ULL), a4);
        local_rbx = 0;
    }
    local_rsp = (local_rsp) + (32);
    return 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0057DE10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0057DE10[BB_0057DE10]
  bb_0057DE67[BB_0057DE67]
  bb_0057DE76[BB_0057DE76]
  bb_0057DE87[BB_0057DE87]
  bb_0057DE95[BB_0057DE95]
  bb_0057DE10 -->|branch| bb_0057DE87
  bb_0057DE10 -->|fallthrough| bb_0057DE67
  bb_0057DE67 -->|branch| bb_0057DE87
  bb_0057DE67 -->|fallthrough| bb_0057DE76
  bb_0057DE76 -->|flow| bb_0057DE87
```
