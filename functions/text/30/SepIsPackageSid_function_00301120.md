# SepIsPackageSid

- RVA: `0x00301120`–`0x0030117D` (길이 `93` bytes)
- VA: `0x0000000140301120`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000730EC`
- 디코드: `30`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0030114F` → [RtlCompareMemory](../6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)

### Direct callers
- [SepMaximumAccessCheck](SepMaximumAccessCheck_function_00300BF0.md) at `0x00300CB4`
- [SepMaximumAccessCheck](SepMaximumAccessCheck_function_00300BF0.md) at `0x00300F9E`
- [SepMaximumAccessCheck](SepMaximumAccessCheck_function_00300BF0.md) at `0x0030107C`
- [SepNormalAccessCheckEx](../3C/SepNormalAccessCheckEx_function_003CFD8C.md) at `0x003CFF27`
- [SepNormalAccessCheckEx](../3C/SepNormalAccessCheckEx_function_003CFD8C.md) at `0x003D013A`
- [SepNormalAccessCheckEx](../3C/SepNormalAccessCheckEx_function_003CFD8C.md) at `0x003D038F`
- [SepNormalAccessCheck](../3D/SepNormalAccessCheck_function_003D0688.md) at `0x003D0800`
- [SepNormalAccessCheck](../3D/SepNormalAccessCheck_function_003D0688.md) at `0x003D08BD`
- [SepNormalAccessCheck](../3D/SepNormalAccessCheck_function_003D0688.md) at `0x003D0B97`
- [SepNormalAccessCheck](../3D/SepNormalAccessCheck_function_003D0688.md) at `0x003D0C31`
- [SepMaximumAccessCheckEx](../60/SepMaximumAccessCheckEx_function_00606D78.md) at `0x00606E84`
- [SepMaximumAccessCheckEx](../60/SepMaximumAccessCheckEx_function_00606D78.md) at `0x00606F28`
- [sub_006E0188](../6E/Unknown_function_006E0188.md) at `0x006E03AF`

### Static image references
- `0x00301131` → RVA `0x00E67D18` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00301120  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00301125  57                              push rdi
00301126  48 83 EC 20                     sub rsp, 0x20
0030112A  80 79 01 02                     cmp byte ptr [rcx + 1], 2
0030112E  48 8B D9                        mov rbx, rcx
00301131  48 8B 3D E0 6B B6 00            mov rdi, qword ptr [rip + 0xb66be0]
00301138  72 20                           jb 0x14030115a
0030113A  0F B6 07                        movzx eax, byte ptr [rdi]
0030113D  38 01                           cmp byte ptr [rcx], al
0030113F  75 19                           jne 0x14030115a
00301141  48 8D 57 02                     lea rdx, [rdi + 2]
00301145  48 83 C1 02                     add rcx, 2
00301149  41 B8 06 00 00 00               mov r8d, 6
0030114F  E8 1C 95 3B 00                  call 0x1406ba670
00301154  48 83 F8 06                     cmp rax, 6
00301158  74 0E                           je 0x140301168
0030115A  32 C0                           xor al, al
0030115C  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00301161  48 83 C4 20                     add rsp, 0x20
00301165  5F                              pop rdi
00301166  C3                              ret
00301167  CC                              int3
00301168  8B 47 08                        mov eax, dword ptr [rdi + 8]
0030116B  39 43 08                        cmp dword ptr [rbx + 8], eax
0030116E  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00301173  0F 94 C0                        sete al
00301176  48 83 C4 20                     add rsp, 0x20
0030117A  5F                              pop rdi
0030117B  C3                              ret
0030117C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepIsPackageSid(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned __int8 *)(a1 + 1)) < 2) goto loc_0030115A;
    if ((*(unsigned __int8 *)(a1)) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11955168))))) goto loc_0030115A;
    a1 = (a1) + (2);
    result = RtlCompareMemory(a1, *(unsigned __int64 *)(v_rip + 11955168) + 2, 6, a4);
    if (result == 6) goto loc_00301168;
loc_0030115A:
    result = 0;
    v_rsp = (v_rsp) + (32);
    return result;
loc_00301168:
    result = ((*(unsigned int *)(v_stack_p8 + 8)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11955168) + 8))))) ? 1 : 0;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepIsPackageSid(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint8_t *)(arg1 + 0x1)) < 2) goto loc_0030115A;
    if ((*(uint8_t *)(arg1)) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xB66BE0))))) goto loc_0030115A;
    Arg1 = (Arg1) + (2);
    result = RtlCompareMemory(Arg1, *(uint64_t *)(v_rip + 0xB66BE0) + 2, 6, a4);
    if (result == 6) goto loc_00301168;
loc_0030115A:
    result = 0;
    local_rsp = (local_rsp) + (32);
    return result;
loc_00301168:
    result = ((*(uint32_t *)(v_stack_p8 + 0x8)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB66BE0) + 0x8))))) ? 1 : 0;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x1` | `8` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00301120&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00301120[BB_00301120]
  bb_0030113A[BB_0030113A]
  bb_00301141[BB_00301141]
  bb_0030115A[BB_0030115A]
  bb_00301167[BB_00301167]
  bb_00301168[BB_00301168]
  bb_0030117C[BB_0030117C]
  bb_00301120 -->|branch| bb_0030115A
  bb_00301120 -->|fallthrough| bb_0030113A
  bb_0030113A -->|branch| bb_0030115A
  bb_0030113A -->|fallthrough| bb_00301141
  bb_00301141 -->|branch| bb_00301168
  bb_00301141 -->|fallthrough| bb_0030115A
  bb_00301167 -->|flow| bb_00301168
```
