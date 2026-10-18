# KiDoubleFaultAbortShadow

- RVA: `0x00BCB540`–`0x00BCB5B7` (길이 `119` bytes)
- VA: `0x0000000140BCB540`
- 실행 섹션: `KVASCODE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C1870`
- 디코드: `33`개 명령, `119/119` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00BCB5B1` → [KiDoubleFaultAbort](../../text/6B/KiDoubleFaultAbort_function_006BF1C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00BCB540  51                              push rcx
00BCB541  50                              push rax
00BCB542  52                              push rdx
00BCB543  B9 01 01 00 C0                  mov ecx, 0xc0000101
00BCB548  0F 32                           rdmsr
00BCB54A  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00BCB54E  89 54 24 5C                     mov dword ptr [rsp + 0x5c], edx
00BCB552  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00BCB557  8B C2                           mov eax, edx
00BCB559  48 C1 EA 20                     shr rdx, 0x20
00BCB55D  B9 01 01 00 C0                  mov ecx, 0xc0000101
00BCB562  0F 30                           wrmsr
00BCB564  0F 20 D8                        mov rax, cr3
00BCB567  65 48 8B 14 25 00 B0 00 00      mov rdx, qword ptr gs:[0xb000]
00BCB570  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00BCB575  48 3B C2                        cmp rax, rdx
00BCB578  74 0F                           je 0x140bcb589
00BCB57A  65 0F BA 24 25 18 B0 00 00 01   bt dword ptr gs:[0xb018], 1
00BCB584  72 03                           jb 0x140bcb589
00BCB586  0F 22 DA                        mov cr3, rdx
00BCB589  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00BCB58E  48 8B 64 24 50                  mov rsp, qword ptr [rsp + 0x50]
00BCB593  FF 71 F8                        push qword ptr [rcx - 8]
00BCB596  FF 71 F0                        push qword ptr [rcx - 0x10]
00BCB599  FF 71 E8                        push qword ptr [rcx - 0x18]
00BCB59C  FF 71 E0                        push qword ptr [rcx - 0x20]
00BCB59F  FF 71 D8                        push qword ptr [rcx - 0x28]
00BCB5A2  FF 71 D0                        push qword ptr [rcx - 0x30]
00BCB5A5  48 8B 51 B8                     mov rdx, qword ptr [rcx - 0x48]
00BCB5A9  48 8B 41 C0                     mov rax, qword ptr [rcx - 0x40]
00BCB5AD  48 8B 49 C8                     mov rcx, qword ptr [rcx - 0x38]
00BCB5B1  E9 0A 3C AF FF                  jmp 0x1406bf1c0
00BCB5B6  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiDoubleFaultAbortShadow(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 v_cr3;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;

    v_stack_p40 = (unsigned int)(result);
    v_stack_p44 = (unsigned int)(a2);
    a2 = (a6) >> (32);
    v_stack_p48 = v_cr3;
    if (v_cr3 == (*(unsigned __int64 *)(gs_base + (0 + 45056)))) goto loc_00BCB589;
    if (v_cr3 >= (*(unsigned __int64 *)(gs_base + (0 + 45056)))) {
        v_cr3 = *(unsigned __int64 *)(gs_base + (0 + 45056));
    }
}
```

## 5. (Beta) C Style

```c
int64_t KiDoubleFaultAbortShadow(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6, int64_t Arg7)
{
    int64_t v_cr3;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;

    v_stack_p40 = (uint32_t)(result);
    v_stack_p44 = (uint32_t)(Arg2);
    Arg2 = (Arg6) >> (32);
    v_stack_p48 = v_cr3;
    if (v_cr3 == (*(uint64_t *)(gs_base + (0 + 0xB000)))) goto loc_00BCB589;
    if (v_cr3 >= (*(uint64_t *)(gs_base + (0 + 0xB000)))) {
        v_cr3 = *(uint64_t *)(gs_base + (0 + 0xB000));
    }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=kvascode&rva=0x00BCB540&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BCB540[BB_00BCB540]
  bb_00BCB57A[BB_00BCB57A]
  bb_00BCB586[BB_00BCB586]
  bb_00BCB589[BB_00BCB589]
  bb_00BCB5B6[BB_00BCB5B6]
  bb_00BCB540 -->|branch| bb_00BCB589
  bb_00BCB540 -->|fallthrough| bb_00BCB57A
  bb_00BCB57A -->|branch| bb_00BCB589
  bb_00BCB57A -->|fallthrough| bb_00BCB586
  bb_00BCB586 -->|flow| bb_00BCB589
```
