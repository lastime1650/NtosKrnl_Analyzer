# MmProbeAndLockSelectedPages

- RVA: `0x0023F790`–`0x0023F815` (길이 `133` bytes)
- VA: `0x000000014023F790`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000615D4`
- 디코드: `33`개 명령, `133/133` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0023F7D3` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- [IopReadFileScatter](../../page/AA/IopReadFileScatter_function_00AA5D78.md) at `0x00AA62E5`
- [IopWriteFileGather](../../page/AA/IopWriteFileGather_function_00AAA95C.md) at `0x00AAAEF3`

### Static image references
- `0x0023F7A8` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0023F80F` → [sub_0023FA4B](Unknown_function_0023FA4B.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0023F790  40 55                           push rbp
0023F792  53                              push rbx
0023F793  56                              push rsi
0023F794  57                              push rdi
0023F795  41 54                           push r12
0023F797  41 55                           push r13
0023F799  48 8D AC 24 D8 EF FF FF         lea rbp, [rsp - 0x1028]
0023F7A1  48 81 EC 28 11 00 00            sub rsp, 0x1128
0023F7A8  48 8B 05 91 AF BC 00            mov rax, qword ptr [rip + 0xbcaf91]
0023F7AF  48 33 C4                        xor rax, rsp
0023F7B2  48 89 85 00 10 00 00            mov qword ptr [rbp + 0x1000], rax
0023F7B9  45 0F B6 E8                     movzx r13d, r8b
0023F7BD  4C 8B E2                        mov r12, rdx
0023F7C0  48 8B F1                        mov rsi, rcx
0023F7C3  33 D2                           xor edx, edx
0023F7C5  41 B8 B0 00 00 00               mov r8d, 0xb0
0023F7CB  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0023F7D0  41 8B D9                        mov ebx, r9d
0023F7D3  E8 68 74 48 00                  call 0x1406c6c40
0023F7D8  8B 4E 28                        mov ecx, dword ptr [rsi + 0x28]
0023F7DB  85 DB                           test ebx, ebx
0023F7DD  B8 00 00 00 00                  mov eax, 0
0023F7E2  BF 01 00 00 00                  mov edi, 1
0023F7E7  0F 44 FB                        cmove edi, ebx
0023F7EA  F7 C1 FF 0F 00 00               test ecx, 0xfff
0023F7F0  0F 95 C0                        setne al
0023F7F3  C1 E9 0C                        shr ecx, 0xc
0023F7F6  03 C1                           add eax, ecx
0023F7F8  48 8D 4D 00                     lea rcx, [rbp]
0023F7FC  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0023F801  48 8D 1C C5 00 00 00 00         lea rbx, [rax*8]
0023F809  48 3D 00 02 00 00               cmp rax, 0x200
0023F80F  0F 87 36 02 00 00               ja 0x14023fa4b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmProbeAndLockSelectedPages(__int64 a1, __int64 a2, unsigned __int8 a3, int a4)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1058;
    unsigned __int64 v_stack_m1108;
    unsigned __int64 v_stack_m1118;
    unsigned __int64 v_stack_m58;

    v_rsp = (v_rsp) - (0x1128ULL);
    result = (*(unsigned __int64 *)(v_rip + 12365713)) ^ (v_rsp);
    v_stack_m58 = result;
    a2 = 0;
    result = memset(v_stack_m1108, a2, 176, a4);
    v_rdi = 1;
    if ((unsigned int)((unsigned int)(a4)) == 0) { v_rdi = (unsigned int)((unsigned int)(a4)); }
    result = ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (0xFFFULL)) != 0) ? 1 : 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 40))) >> (12));
    result = (unsigned int)((result) + ((unsigned int)(a1)));
    v_stack_m1118 = v_stack_m1058;
}
```

## 5. (Beta) C Style

```c
int64_t MmProbeAndLockSelectedPages(void *Arg1, int64_t Arg2, uint8_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m1058;
    uint64_t v_stack_m1108;
    uint64_t v_stack_m1118;
    uint64_t v_stack_m58;

    local_rsp = (local_rsp) - (0x1128ULL);
    result = (*(uint64_t *)(v_rip + 0xBCAF91)) ^ (local_rsp);
    v_stack_m58 = result;
    Arg2 = 0;
    result = memset(v_stack_m1108, Arg2, 176, Arg4);
    local_rdi = 1;
    if ((uint32_t)((uint32_t)(Arg4)) == 0) { local_rdi = (uint32_t)((uint32_t)(Arg4)); }
    result = ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (0xFFFULL)) != 0) ? 1 : 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x28))) >> (12));
    result = (uint32_t)((result) + ((uint32_t)(Arg1)));
    v_stack_m1118 = v_stack_m1058;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0023F790&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0023F790[BB_0023F790]
```
