# KiMcheckAbortShadow

- RVA: `0x00BCB9C0`–`0x00BCBA36` (길이 `118` bytes)
- VA: `0x0000000140BCB9C0`
- 실행 섹션: `KVASCODE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C18E0`
- 디코드: `33`개 명령, `118/118` bytes 표시
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
  - `0x00BCBA30` → [KiMcheckAbort](../../text/6C/KiMcheckAbort_function_006C16C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00BCB9C0  41 50                           push r8
00BCB9C2  51                              push rcx
00BCB9C3  50                              push rax
00BCB9C4  52                              push rdx
00BCB9C5  B9 01 01 00 C0                  mov ecx, 0xc0000101
00BCB9CA  0F 32                           rdmsr
00BCB9CC  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00BCB9D0  89 54 24 5C                     mov dword ptr [rsp + 0x5c], edx
00BCB9D4  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00BCB9D9  8B C2                           mov eax, edx
00BCB9DB  48 C1 EA 20                     shr rdx, 0x20
00BCB9DF  B9 01 01 00 C0                  mov ecx, 0xc0000101
00BCB9E4  0F 30                           wrmsr
00BCB9E6  0F 20 D8                        mov rax, cr3
00BCB9E9  65 48 8B 14 25 00 B0 00 00      mov rdx, qword ptr gs:[0xb000]
00BCB9F2  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00BCB9F7  48 3B C2                        cmp rax, rdx
00BCB9FA  74 0F                           je 0x140bcba0b
00BCB9FC  65 0F BA 24 25 18 B0 00 00 01   bt dword ptr gs:[0xb018], 1
00BCBA06  72 03                           jb 0x140bcba0b
00BCBA08  0F 22 DA                        mov cr3, rdx
00BCBA0B  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00BCBA10  48 8B 64 24 50                  mov rsp, qword ptr [rsp + 0x50]
00BCBA15  FF 71 F8                        push qword ptr [rcx - 8]
00BCBA18  FF 71 F0                        push qword ptr [rcx - 0x10]
00BCBA1B  FF 71 E8                        push qword ptr [rcx - 0x18]
00BCBA1E  FF 71 E0                        push qword ptr [rcx - 0x20]
00BCBA21  FF 71 D8                        push qword ptr [rcx - 0x28]
00BCBA24  48 8B 51 B8                     mov rdx, qword ptr [rcx - 0x48]
00BCBA28  48 8B 41 C0                     mov rax, qword ptr [rcx - 0x40]
00BCBA2C  48 8B 49 C8                     mov rcx, qword ptr [rcx - 0x38]
00BCBA30  E9 8B 5C AF FF                  jmp 0x1406c16c0
00BCBA35  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiMcheckAbortShadow(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 v_cr3;
    unsigned int v_stack_p38;
    unsigned int v_stack_p3C;
    unsigned __int64 v_stack_p40;

    v_stack_p38 = (unsigned int)(result);
    v_stack_p3C = (unsigned int)(a2);
    a2 = (a5) >> (32);
    v_stack_p40 = v_cr3;
    if (v_cr3 == (*(unsigned __int64 *)(gs_base + (0 + 45056)))) goto loc_00BCBA0B;
    if (v_cr3 >= (*(unsigned __int64 *)(gs_base + (0 + 45056)))) {
        v_cr3 = *(unsigned __int64 *)(gs_base + (0 + 45056));
    }
}
```

## 5. (Beta) C Style

```c
int64_t KiMcheckAbortShadow(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    int64_t v_cr3;
    uint32_t v_stack_p38;
    uint32_t v_stack_p3C;
    uint64_t v_stack_p40;

    v_stack_p38 = (uint32_t)(result);
    v_stack_p3C = (uint32_t)(Arg2);
    Arg2 = (Arg5) >> (32);
    v_stack_p40 = v_cr3;
    if (v_cr3 == (*(uint64_t *)(gs_base + (0 + 0xB000)))) goto loc_00BCBA0B;
    if (v_cr3 >= (*(uint64_t *)(gs_base + (0 + 0xB000)))) {
        v_cr3 = *(uint64_t *)(gs_base + (0 + 0xB000));
    }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=kvascode&rva=0x00BCB9C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BCB9C0[BB_00BCB9C0]
  bb_00BCB9FC[BB_00BCB9FC]
  bb_00BCBA08[BB_00BCBA08]
  bb_00BCBA0B[BB_00BCBA0B]
  bb_00BCBA35[BB_00BCBA35]
  bb_00BCB9C0 -->|branch| bb_00BCBA0B
  bb_00BCB9C0 -->|fallthrough| bb_00BCB9FC
  bb_00BCB9FC -->|branch| bb_00BCBA0B
  bb_00BCB9FC -->|fallthrough| bb_00BCBA08
  bb_00BCBA08 -->|flow| bb_00BCBA0B
```
