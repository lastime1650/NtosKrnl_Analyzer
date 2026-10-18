# KiReleaseCpuPartitionAssignmentLock

- RVA: `0x0043F9C0`–`0x0043F9F4` (길이 `52` bytes)
- VA: `0x000000014043F9C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0043F9D0` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x0043F9E4` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)

### Direct callers
- [KiQueryCpuPartitionAffinityProcess](../3C/KiQueryCpuPartitionAffinityProcess_function_003C01A0.md) at `0x003C0242`
- [KiRemoveAndFreeCpuPartitionAssignmentProcess](KiRemoveAndFreeCpuPartitionAssignmentProcess_function_0043F8C0.md) at `0x0043F8FE`
- [KiAvailableCpusPartitionWorkItemCallback](../5B/KiAvailableCpusPartitionWorkItemCallback_function_005B9990.md) at `0x005B9A73`
- [KeAssignCpuPartitionsToProcess](../5C/KeAssignCpuPartitionsToProcess_function_005C08D0.md) at `0x005C0A8C`

### Static image references
- `0x0043F9C9` → RVA `0x00F23448` (`.data`; read)
- `0x0043F9D5` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043F9C0  40 53                           push rbx
0043F9C2  48 83 EC 20                     sub rsp, 0x20
0043F9C6  0F B6 D9                        movzx ebx, cl
0043F9C9  48 8D 0D 78 3A AE 00            lea rcx, [rip + 0xae3a78]
0043F9D0  E8 9B 6C DC FF                  call 0x140206670
0043F9D5  83 3D 44 73 B8 00 00            cmp dword ptr [rip + 0xb87344], 0
0043F9DC  74 0B                           je 0x14043f9e9
0043F9DE  44 0F 20 C1                     mov rcx, cr8
0043F9E2  8A D3                           mov dl, bl
0043F9E4  E8 AF 5C 0B 00                  call 0x1404f5698
0043F9E9  44 0F 22 C3                     mov cr8, rbx
0043F9ED  48 83 C4 20                     add rsp, 0x20
0043F9F1  5B                              pop rbx
0043F9F2  C3                              ret
0043F9F3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiReleaseCpuPartitionAssignmentLock(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = KxReleaseSpinLock(v_rip + 11418232, a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 12088132)) != 0) {
        a1 = v_cr8;
        a2 = a1;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiReleaseCpuPartitionAssignmentLock(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = KxReleaseSpinLock(v_rip + 11418232, a2, a3, a4);
    if ((*(uint32_t *)(v_rip + 0xB87344)) != 0) {
        Arg1 = v_cr8;
        a2 = Arg1;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043F9C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043F9C0[BB_0043F9C0]
  bb_0043F9DE[BB_0043F9DE]
  bb_0043F9E9[BB_0043F9E9]
  bb_0043F9F3[BB_0043F9F3]
  bb_0043F9C0 -->|branch| bb_0043F9E9
  bb_0043F9C0 -->|fallthrough| bb_0043F9DE
  bb_0043F9DE -->|flow| bb_0043F9E9
```
