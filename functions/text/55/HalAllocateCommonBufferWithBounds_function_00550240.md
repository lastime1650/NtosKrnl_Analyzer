# HalAllocateCommonBufferWithBounds

- RVA: `0x00550240`–`0x00550299` (길이 `89` bytes)
- VA: `0x0000000140550240`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CC98`
- 디코드: `19`개 명령, `89/89` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00550289` → [HalpAllocateDomainCommonBufferInternal](../3E/HalpAllocateDomainCommonBufferInternal_function_003E8B64.md) (function, `0x003E8B64`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00550240  4C 8B DC                        mov r11, rsp
00550243  48 83 EC 58                     sub rsp, 0x58
00550247  49 83 63 08 00                  and qword ptr [r11 + 8], 0
0055024C  49 8D 43 08                     lea rax, [r11 + 8]
00550250  48 8B 89 00 02 00 00            mov rcx, qword ptr [rcx + 0x200]
00550257  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0055025B  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00550263  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00550267  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
0055026E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00550272  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0055027A  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
0055027E  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
00550285  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00550289  E8 D6 88 E9 FF                  call 0x1403e8b64
0055028E  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00550293  48 83 C4 58                     add rsp, 0x58
00550297  C3                              ret
00550298  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalAllocateCommonBufferWithBounds(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m28;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (88);
    *(unsigned __int64 *)(v_rsp - 24) = v_rsp + 8;
    *(unsigned __int64 *)(v_rsp - 32) = a8;
    v_stack_m28 = (unsigned int)((unsigned int)(a7));
    *(unsigned __int64 *)(v_rsp - 48) = a6;
    v_stack_m38 = (unsigned int)((unsigned int)(a5));
    result = HalpAllocateDomainCommonBufferInternal(*(unsigned __int64 *)(a1 + 512), a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return v_stack_p8;
}
```

## 5. (Beta) C Style

```c
int64_t HalAllocateCommonBufferWithBounds(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6, uint32_t Arg7, int64_t Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m28;
    uint32_t v_stack_m38;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (88);
    *(uint64_t *)(local_rsp - 0x18) = local_rsp + 8;
    *(uint64_t *)(local_rsp - 0x20) = Arg8;
    v_stack_m28 = (uint32_t)((uint32_t)(Arg7));
    *(uint64_t *)(local_rsp - 0x30) = Arg6;
    v_stack_m38 = (uint32_t)((uint32_t)(Arg5));
    result = HalpAllocateDomainCommonBufferInternal(*(uint64_t *)(arg1 + 0x200), Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return v_stack_p8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x200` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00550240&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00550240[BB_00550240]
  bb_00550298[BB_00550298]
```
