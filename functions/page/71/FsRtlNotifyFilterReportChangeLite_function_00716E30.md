# FsRtlNotifyFilterReportChangeLite

- RVA: `0x00716E30`–`0x00716E80` (길이 `80` bytes)
- VA: `0x0000000140716E30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C2A4`
- 디코드: `16`개 명령, `80/80` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00716E75` → [FsRtlNotifyFilterReportChangeLiteEx](../A1/FsRtlNotifyFilterReportChangeLiteEx_function_00A1F2B0.md) (function, `0x00A1F2B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00716E30  48 83 EC 58                     sub rsp, 0x58
00716E34  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
00716E3A  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
00716E41  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00716E45  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00716E4D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00716E52  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
00716E5A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00716E5F  8B 84 24 88 00 00 00            mov eax, dword ptr [rsp + 0x88]
00716E66  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00716E6A  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
00716E71  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00716E75  E8 36 84 30 00                  call 0x140a1f2b0
00716E7A  48 83 C4 58                     add rsp, 0x58
00716E7E  C3                              ret
00716E7F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlNotifyFilterReportChangeLite(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, __int64 a7, __int64 a8, unsigned int a9)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned int v_stack_m38;

    v_rsp = (v_rsp) - (88);
    v_stack_m18 = (unsigned int)((unsigned int)(a9));
    v_stack_m20 = a8;
    v_stack_m28 = a7;
    v_stack_m30 = (unsigned int)((unsigned int)(a6));
    v_stack_m38 = (unsigned int)((unsigned int)(a5));
    result = FsRtlNotifyFilterReportChangeLiteEx(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlNotifyFilterReportChangeLite(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, int64_t Arg7, int64_t Arg8, uint32_t Arg9)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint32_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    v_stack_m18 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m20 = Arg8;
    v_stack_m28 = Arg7;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m38 = (uint32_t)((uint32_t)(Arg5));
    result = FsRtlNotifyFilterReportChangeLiteEx(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00716E30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00716E30[BB_00716E30]
  bb_00716E7F[BB_00716E7F]
```
