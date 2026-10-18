# MiPteForProtoPoolMadeDemandFill

- RVA: `0x004A378C`–`0x004A3808` (길이 `124` bytes)
- VA: `0x00000001404A378C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `25`개 명령, `124/124` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004A37B7` → [MiMapPageInHyperSpaceWorker](../33/MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)

### Direct callers
- [MiWsleFlush](../23/MiWsleFlush_function_0023FB30.md) at `0x0023FE93`

### Static image references
- `0x004A37F0` → RVA `0x00010880` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A378C  48 83 EC 28                     sub rsp, 0x28
004A3790  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004A379A  48 2B C8                        sub rcx, rax
004A379D  33 D2                           xor edx, edx
004A379F  48 C1 F9 04                     sar rcx, 4
004A37A3  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
004A37AD  48 0F AF C8                     imul rcx, rax
004A37B1  41 B8 00 00 00 80               mov r8d, 0x80000000
004A37B7  E8 54 F3 E8 FF                  call 0x140332b10
004A37BC  4C 8B C0                        mov r8, rax
004A37BF  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
004A37C9  49 C1 E8 09                     shr r8, 9
004A37CD  4C 23 C1                        and r8, rcx
004A37D0  48 8B 00                        mov rax, qword ptr [rax]
004A37D3  48 B9 00 00 00 00 80 F6 FF FF   movabs rcx, 0xfffff68000000000
004A37DD  4C 03 C1                        add r8, rcx
004A37E0  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
004A37E9  48 8B 91 38 88 00 00            mov rdx, qword ptr [rcx + 0x8838]
004A37F0  48 8B 0D 89 D0 B6 FF            mov rcx, qword ptr [rip - 0x492f77]
004A37F7  48 83 22 00                     and qword ptr [rdx], 0
004A37FB  48 83 C8 02                     or rax, 2
004A37FF  49 89 08                        mov qword ptr [r8], rcx
004A3802  48 83 C4 28                     add rsp, 0x28
004A3806  C3                              ret
004A3807  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPteForProtoPoolMadeDemandFill(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (a1) - (result);
    a2 = 0;
    a1 = (a1) >> (4);
    a1 = (a1) * (result);
    result = MiMapPageInHyperSpaceWorker(a1, a2, (unsigned int)(0x80000000ULL), a4);
    a3 = (result) >> (9);
    a3 = (a3) & (a1);
    a3 = (a3) + (a1);
    result = (*(unsigned __int64 *)(result)) | (2);
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(v_rip - 4796279);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiPteForProtoPoolMadeDemandFill(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (Arg1) - (result);
    Arg2 = 0;
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (result);
    result = MiMapPageInHyperSpaceWorker(Arg1, Arg2, (uint32_t)(0x80000000ULL), a4);
    a3 = (result) >> (9);
    a3 = (a3) & (Arg1);
    a3 = (a3) + (Arg1);
    result = (*(uint64_t *)(result)) | (2);
    *(uint64_t *)(a3) = *(uint64_t *)(v_rip - 0x492F77);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A378C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A378C[BB_004A378C]
  bb_004A3807[BB_004A3807]
```
