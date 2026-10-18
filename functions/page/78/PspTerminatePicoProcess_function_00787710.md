# PspTerminatePicoProcess

- RVA: `0x00787710`–`0x00787754` (길이 `68` bytes)
- VA: `0x0000000140787710`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `19`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00787737` → [PspTerminateProcess](../90/PspTerminateProcess_function_00903FFC.md) (function, `0x00903FFC`)
- `0x00787741` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00787741` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00787710  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00787715  57                              push rdi
00787716  48 83 EC 20                     sub rsp, 0x20
0078771A  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
00787723  44 8B C2                        mov r8d, edx
00787726  41 B9 08 00 00 00               mov r9d, 8
0078772C  48 8B D7                        mov rdx, rdi
0078772F  66 FF 8F E4 01 00 00            dec word ptr [rdi + 0x1e4]
00787736  90                              nop
00787737  E8 C0 C8 17 00                  call 0x140903ffc
0078773C  48 8B CF                        mov rcx, rdi
0078773F  8B D8                           mov ebx, eax
00787741  E8 CA 78 AD FF                  call 0x14025f010
00787746  8B C3                           mov eax, ebx
00787748  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0078774D  48 83 C4 20                     add rsp, 0x20
00787751  5F                              pop rdi
00787752  C3                              ret
00787753  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspTerminatePicoProcess(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = PspTerminateProcess(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(a2), 8);
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(a2), 8);
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t PspTerminatePicoProcess(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = PspTerminateProcess(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(Arg2), 8);
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(Arg2), 8);
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00787710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00787710[BB_00787710]
  bb_00787753[BB_00787753]
```
