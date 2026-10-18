# KiCpuPartitionCheckGenericDpc

- RVA: `0x005C159C`–`0x005C15CE` (길이 `50` bytes)
- VA: `0x00000001405C159C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x005C15B6` → [KeIsEqualAffinityEx](../30/KeIsEqualAffinityEx_function_00305230.md) (function, `0x00305230`)
- `0x005C15C2` → [EtwTraceCpuPartitionGenericDpcViolation](../64/EtwTraceCpuPartitionGenericDpcViolation_function_0064F8A4.md) (function, `0x0064F8A4`)

### Direct callers
- [KeGenericCallDpcEx](../2C/KeGenericCallDpcEx_function_002C99F4.md) at `0x002C9B43`
- [KeSwapDirectoryTableBase](../46/KeSwapDirectoryTableBase_function_0046590C.md) at `0x0046599E`
- [KeGenericCallDpc](../49/KeGenericCallDpc_function_0049F980.md) at `0x0049F9CB`

### Static image references
- `0x005C15A5` → RVA `0x00FC7120` (`ALMOSTRO`; read)
- `0x005C15AC` → RVA `0x00FC6C20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005C159C  40 53                           push rbx
005C159E  48 83 EC 20                     sub rsp, 0x20
005C15A2  48 8B D9                        mov rbx, rcx
005C15A5  48 8D 15 74 5B A0 00            lea rdx, [rip + 0xa05b74]
005C15AC  48 8B 0D 6D 56 A0 00            mov rcx, qword ptr [rip + 0xa0566d]
005C15B3  48 8B 09                        mov rcx, qword ptr [rcx]
005C15B6  E8 75 3C D4 FF                  call 0x140305230
005C15BB  85 C0                           test eax, eax
005C15BD  75 08                           jne 0x1405c15c7
005C15BF  48 8B CB                        mov rcx, rbx
005C15C2  E8 DD E2 08 00                  call 0x14064f8a4
005C15C7  48 83 C4 20                     add rsp, 0x20
005C15CB  5B                              pop rbx
005C15CC  C3                              ret
005C15CD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiCpuPartitionCheckGenericDpc(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = KeIsEqualAffinityEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10507885)), v_rip + 10509172, a3, a4);
    if ((unsigned int)(result) == 0) {
        a1 = a1;
        result = EtwTraceCpuPartitionGenericDpcViolation(a1, v_rip + 10509172, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiCpuPartitionCheckGenericDpc(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = KeIsEqualAffinityEx(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA0566D)), v_rip + 10509172, a3, a4);
    if ((uint32_t)(result) == 0) {
        Arg1 = Arg1;
        result = EtwTraceCpuPartitionGenericDpcViolation(Arg1, v_rip + 10509172, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005C159C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005C159C[BB_005C159C]
  bb_005C15BF[BB_005C15BF]
  bb_005C15C7[BB_005C15C7]
  bb_005C15CD[BB_005C15CD]
  bb_005C159C -->|branch| bb_005C15C7
  bb_005C159C -->|fallthrough| bb_005C15BF
  bb_005C15BF -->|flow| bb_005C15C7
```
