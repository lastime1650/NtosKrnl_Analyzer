# MiReadyFlushMdlToWrite

- RVA: `0x00404664`–`0x00404711` (길이 `173` bytes)
- VA: `0x0000000140404664`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007A3F0`
- 디코드: `45`개 명령, `173/173` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004046B2` → [MiStartingOffset](../34/MiStartingOffset_function_003482E0.md) (function, `0x003482E0`)
- `0x004046BD` → [MiEndingOffsetWithLock](MiEndingOffsetWithLock_function_00404718.md) (function, `0x00404718`)

### Direct callers
- [MiFlushSection](MiFlushSection_function_004036B0.md) at `0x00403C62`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00404664  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00404669  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0040466E  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00404673  57                              push rdi
00404674  48 83 EC 20                     sub rsp, 0x20
00404678  48 8B 41 30                     mov rax, qword ptr [rcx + 0x30]
0040467C  41 8B F8                        mov edi, r8d
0040467F  48 8B DA                        mov rbx, rdx
00404682  48 8B F1                        mov rsi, rcx
00404685  4C 8D 0C 40                     lea r9, [rax + rax*2]
00404689  4D 03 C9                        add r9, r9
0040468C  48 B8 08 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000008
00404696  4A 8B 14 C8                     mov rdx, qword ptr [rax + r9*8]
0040469A  41 83 C8 FF                     or r8d, 0xffffffff
0040469E  83 61 2C 00                     and dword ptr [rcx + 0x2c], 0
004046A2  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
004046AC  48 0B D0                        or rdx, rax
004046AF  48 8B CB                        mov rcx, rbx
004046B2  E8 29 3C F4 FF                  call 0x1403482e0
004046B7  48 8B CB                        mov rcx, rbx
004046BA  48 8B E8                        mov rbp, rax
004046BD  E8 56 00 00 00                  call 0x140404718
004046C2  0F B7 4E 0A                     movzx ecx, word ptr [rsi + 0xa]
004046C6  66 83 C9 02                     or cx, 2
004046CA  66 89 4E 0A                     mov word ptr [rsi + 0xa], cx
004046CE  0F B7 D1                        movzx edx, cx
004046D1  40 F6 C7 08                     test dil, 8
004046D5  75 2C                           jne 0x140404703
004046D7  8B 46 28                        mov eax, dword ptr [rsi + 0x28]
004046DA  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004046DF  48 C1 E0 03                     shl rax, 3
004046E3  48 C1 E8 0C                     shr rax, 0xc
004046E7  66 83 C0 30                     add ax, 0x30
004046EB  66 89 46 08                     mov word ptr [rsi + 8], ax
004046EF  48 8B C5                        mov rax, rbp
004046F2  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
004046F7  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
004046FC  48 83 C4 20                     add rsp, 0x20
00404700  5F                              pop rdi
00404701  C3                              ret
00404702  CC                              int3
00404703  B8 00 40 00 00                  mov eax, 0x4000
00404708  66 0B D0                        or dx, ax
0040470B  66 89 56 0A                     mov word ptr [rsi + 0xa], dx
0040470F  EB C6                           jmp 0x1404046d7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReadyFlushMdlToWrite(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a4 = (*(unsigned __int64 *)(a1 + 48) + *(unsigned __int64 *)(a1 + 48) * 2) + (*(unsigned __int64 *)(a1 + 48) + *(unsigned __int64 *)(a1 + 48) * 2);
    a3 = (unsigned int)((a3) | (0xFFFFFFFFULL));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + a4 * 8)) | (*(unsigned __int64 *)(a1 + 48));
    result = MiStartingOffset(a2, a2, a3, a4);
    result = MiEndingOffsetWithLock(a2, a2, a3, a4);
    a1 = (unsigned __int16)((*(unsigned __int16 *)(a1 + 10)) | (2));
    *(unsigned __int16 *)(a1 + 10) = (unsigned __int16)(a1);
    if ((((unsigned __int8)((unsigned int)(a3))) & (8)) != 0) goto loc_00404703;
loc_004046D7:
    result = ((unsigned int)(*(unsigned int *)(a1 + 40))) << (3);
    result = (result) >> (12);
    result = (unsigned __int16)((result) + (48));
    *(unsigned __int16 *)(a1 + 8) = (unsigned __int16)(result);
    v_rsp = (v_rsp) + (32);
    return result;
loc_00404703:
    a2 = (unsigned __int16)(((unsigned __int16)(a1)) | ((unsigned __int16)((unsigned int)(0x4000ULL))));
    *(unsigned __int16 *)(v_stack_p18 + 10) = (unsigned __int16)(a2);
    goto loc_004046D7;
}
```

## 5. (Beta) C Style

```c
int64_t MiReadyFlushMdlToWrite(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    a4 = (*(uint64_t *)(arg1 + 0x30) + *(uint64_t *)(arg1 + 0x30) * 2) + (*(uint64_t *)(arg1 + 0x30) + *(uint64_t *)(arg1 + 0x30) * 2);
    Arg3 = (uint32_t)((Arg3) | (0xFFFFFFFFULL));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + a4 * 8)) | (*(uint64_t *)(arg1 + 0x30));
    result = MiStartingOffset(Arg2, Arg2, Arg3, a4);
    result = MiEndingOffsetWithLock(Arg2, Arg2, Arg3, a4);
    Arg1 = (uint16_t)((*(uint16_t *)(arg1 + 0xA)) | (2));
    *(uint16_t *)(arg1 + 0xA) = (uint16_t)(Arg1);
    if ((((uint8_t)((uint32_t)(Arg3))) & (8)) != 0) goto loc_00404703;
loc_004046D7:
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x28))) << (3);
    result = (result) >> (12);
    result = (uint16_t)((result) + (48));
    *(uint16_t *)(arg1 + 0x8) = (uint16_t)(result);
    local_rsp = (local_rsp) + (32);
    return result;
loc_00404703:
    Arg2 = (uint16_t)(((uint16_t)(Arg1)) | ((uint16_t)((uint32_t)(0x4000ULL))));
    *(uint16_t *)(v_stack_p18 + 0xA) = (uint16_t)(Arg2);
    goto loc_004046D7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `16` | `W` |
| `Arg1` | `+ 0xA` | `16` | `R` |
| `Arg1` | `+ 0xA` | `16` | `W` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R/W` |
| `Arg1` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00404664&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00404664[BB_00404664]
  bb_004046D7[BB_004046D7]
  bb_00404702[BB_00404702]
  bb_00404703[BB_00404703]
  bb_00404664 -->|branch| bb_00404703
  bb_00404664 -->|fallthrough| bb_004046D7
  bb_00404702 -->|flow| bb_00404703
  bb_00404703 -->|branch| bb_004046D7
```
