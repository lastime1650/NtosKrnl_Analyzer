# KiNmiInterruptShadow

- RVA: `0x00BCB240`–`0x00BCB2B6` (길이 `118` bytes)
- VA: `0x0000000140BCB240`
- 실행 섹션: `KVASCODE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C1820`
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
  - `0x00BCB2B0` → [KiNmiInterrupt](../../text/6B/KiNmiInterrupt_function_006BD3C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00BCB240  41 50                           push r8
00BCB242  51                              push rcx
00BCB243  50                              push rax
00BCB244  52                              push rdx
00BCB245  B9 01 01 00 C0                  mov ecx, 0xc0000101
00BCB24A  0F 32                           rdmsr
00BCB24C  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00BCB250  89 54 24 5C                     mov dword ptr [rsp + 0x5c], edx
00BCB254  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00BCB259  8B C2                           mov eax, edx
00BCB25B  48 C1 EA 20                     shr rdx, 0x20
00BCB25F  B9 01 01 00 C0                  mov ecx, 0xc0000101
00BCB264  0F 30                           wrmsr
00BCB266  0F 20 D8                        mov rax, cr3
00BCB269  65 48 8B 14 25 00 B0 00 00      mov rdx, qword ptr gs:[0xb000]
00BCB272  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00BCB277  48 3B C2                        cmp rax, rdx
00BCB27A  74 0F                           je 0x140bcb28b
00BCB27C  65 0F BA 24 25 18 B0 00 00 01   bt dword ptr gs:[0xb018], 1
00BCB286  72 03                           jb 0x140bcb28b
00BCB288  0F 22 DA                        mov cr3, rdx
00BCB28B  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00BCB290  48 8B 64 24 50                  mov rsp, qword ptr [rsp + 0x50]
00BCB295  FF 71 F8                        push qword ptr [rcx - 8]
00BCB298  FF 71 F0                        push qword ptr [rcx - 0x10]
00BCB29B  FF 71 E8                        push qword ptr [rcx - 0x18]
00BCB29E  FF 71 E0                        push qword ptr [rcx - 0x20]
00BCB2A1  FF 71 D8                        push qword ptr [rcx - 0x28]
00BCB2A4  48 8B 51 B8                     mov rdx, qword ptr [rcx - 0x48]
00BCB2A8  48 8B 41 C0                     mov rax, qword ptr [rcx - 0x40]
00BCB2AC  48 8B 49 C8                     mov rcx, qword ptr [rcx - 0x38]
00BCB2B0  E9 0B 21 AF FF                  jmp 0x1406bd3c0
00BCB2B5  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiNmiInterruptShadow(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 v_cr3;
    unsigned int v_stack_p38;
    unsigned int v_stack_p3C;
    unsigned __int64 v_stack_p40;

    v_stack_p38 = (unsigned int)(result);
    v_stack_p3C = (unsigned int)(a2);
    a2 = (a5) >> (32);
    v_stack_p40 = v_cr3;
    if (v_cr3 == (*(unsigned __int64 *)(gs_base + (0 + 45056)))) goto loc_00BCB28B;
    if (v_cr3 >= (*(unsigned __int64 *)(gs_base + (0 + 45056)))) {
        v_cr3 = *(unsigned __int64 *)(gs_base + (0 + 45056));
    }
}
```

## 5. (Beta) C Style

```c
int64_t KiNmiInterruptShadow(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    int64_t v_cr3;
    uint32_t v_stack_p38;
    uint32_t v_stack_p3C;
    uint64_t v_stack_p40;

    v_stack_p38 = (uint32_t)(result);
    v_stack_p3C = (uint32_t)(Arg2);
    Arg2 = (Arg5) >> (32);
    v_stack_p40 = v_cr3;
    if (v_cr3 == (*(uint64_t *)(gs_base + (0 + 0xB000)))) goto loc_00BCB28B;
    if (v_cr3 >= (*(uint64_t *)(gs_base + (0 + 0xB000)))) {
        v_cr3 = *(uint64_t *)(gs_base + (0 + 0xB000));
    }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=kvascode&rva=0x00BCB240&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BCB240[BB_00BCB240]
  bb_00BCB27C[BB_00BCB27C]
  bb_00BCB288[BB_00BCB288]
  bb_00BCB28B[BB_00BCB28B]
  bb_00BCB2B5[BB_00BCB2B5]
  bb_00BCB240 -->|branch| bb_00BCB28B
  bb_00BCB240 -->|fallthrough| bb_00BCB27C
  bb_00BCB27C -->|branch| bb_00BCB28B
  bb_00BCB27C -->|fallthrough| bb_00BCB288
  bb_00BCB288 -->|flow| bb_00BCB28B
```
