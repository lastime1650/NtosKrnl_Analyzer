# HalpAcpiInitDiscard

- RVA: `0x00C1FA54`–`0x00C1FA7F` (길이 `43` bytes)
- VA: `0x0000000140C1FA54`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00C1FA74` → [HalpSetupAcpiPhase0](../C2/HalpSetupAcpiPhase0_function_00C23EDC.md) (function, `0x00C23EDC`)

### Direct callers
- [HalpAcpiInitSystem](../../pagelk/B5/HalpAcpiInitSystem_function_00B5D390.md) at `0x00B5D3FA`

### Static image references
- `0x00C1FA58` → RVA `0x0070BAE0` (`HaliInitPowerManagement`; read)
- `0x00C1FA5F` → RVA `0x00E00698` (`.data`; write)
- `0x00C1FA66` → RVA `0x0053E9F0` (`HalAcpiGetRsdpDispatch`; read)
- `0x00C1FA6D` → RVA `0x00E00B00` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C1FA54  48 83 EC 28                     sub rsp, 0x28
00C1FA58  48 8D 05 81 C0 AE FF            lea rax, [rip - 0x513f7f]
00C1FA5F  48 89 05 32 0C 1E 00            mov qword ptr [rip + 0x1e0c32], rax
00C1FA66  48 8D 05 83 EF 91 FF            lea rax, [rip - 0x6e107d]
00C1FA6D  48 89 05 8C 10 1E 00            mov qword ptr [rip + 0x1e108c], rax
00C1FA74  E8 63 44 00 00                  call 0x140c23edc
00C1FA79  48 83 C4 28                     add rsp, 0x28
00C1FA7D  C3                              ret
00C1FA7E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpAcpiInitDiscard(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    *(unsigned __int64 *)(v_rip + 1969202) = v_rip - 5324671;
    *(unsigned __int64 *)(v_rip + 1970316) = v_rip - 7213181;
    result = HalpSetupAcpiPhase0(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpAcpiInitDiscard(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    *(uint64_t *)(v_rip + 0x1E0C32) = v_rip - 5324671;
    *(uint64_t *)(v_rip + 0x1E108C) = v_rip - 7213181;
    result = HalpSetupAcpiPhase0(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C1FA54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C1FA54[BB_00C1FA54]
  bb_00C1FA7E[BB_00C1FA7E]
```
