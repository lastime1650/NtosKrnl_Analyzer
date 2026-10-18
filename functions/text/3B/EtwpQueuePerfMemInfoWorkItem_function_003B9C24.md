# EtwpQueuePerfMemInfoWorkItem

- RVA: `0x003B9C24`–`0x003B9C6D` (길이 `73` bytes)
- VA: `0x00000001403B9C24`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `21`개 명령, `73/73` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003B9C3B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x003B9C61` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- [EtwpLogMemInfoTimerCallback](EtwpLogMemInfoTimerCallback_function_003B9850.md) at `0x003B98A8`

### Static image references
- `0x003B9C49` → RVA `0x0091D5C0` (`EtwpPerfMemInfoWork`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x003B9C3B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003B9C24  40 53                           push rbx
003B9C26  48 83 EC 20                     sub rsp, 0x20
003B9C2A  BA 28 00 00 00                  mov edx, 0x28
003B9C2F  48 8B D9                        mov rbx, rcx
003B9C32  41 B8 45 74 77 57               mov r8d, 0x57777445
003B9C38  8D 4A 18                        lea ecx, [rdx + 0x18]
003B9C3B  E8 B0 84 7C 00                  call 0x140b820f0
003B9C40  48 85 C0                        test rax, rax
003B9C43  74 21                           je 0x1403b9c66
003B9C45  48 83 20 00                     and qword ptr [rax], 0
003B9C49  48 8D 0D 70 39 56 00            lea rcx, [rip + 0x563970]
003B9C50  48 89 48 10                     mov qword ptr [rax + 0x10], rcx
003B9C54  33 D2                           xor edx, edx
003B9C56  48 8B C8                        mov rcx, rax
003B9C59  48 89 58 20                     mov qword ptr [rax + 0x20], rbx
003B9C5D  48 89 40 18                     mov qword ptr [rax + 0x18], rax
003B9C61  E8 BA F8 F3 FF                  call 0x1402f9520
003B9C66  48 83 C4 20                     add rsp, 0x20
003B9C6A  5B                              pop rbx
003B9C6B  C3                              ret
003B9C6C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpQueuePerfMemInfoWorkItem(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ExAllocatePool2(40 + 24, 40, (unsigned int)(0x57777445ULL), a4);
    if (result != 0) {
        a1 = v_rip + 5650800;
        *(unsigned __int64 *)(result + 16) = a1;
        a2 = 0;
        a1 = result;
        *(unsigned __int64 *)(result + 32) = a1;
        *(unsigned __int64 *)(result + 24) = result;
        result = ExQueueWorkItem(a1, a2, (unsigned int)(0x57777445ULL), a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpQueuePerfMemInfoWorkItem(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ExAllocatePool2(40 + 24, 40, (uint32_t)(0x57777445ULL), a4);
    if (result != 0) {
        Arg1 = v_rip + 5650800;
        *(uint64_t *)(result + 0x10) = Arg1;
        a2 = 0;
        Arg1 = result;
        *(uint64_t *)(result + 0x20) = Arg1;
        *(uint64_t *)(result + 0x18) = result;
        result = ExQueueWorkItem(Arg1, a2, (uint32_t)(0x57777445ULL), a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003B9C24&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003B9C24[BB_003B9C24]
  bb_003B9C45[BB_003B9C45]
  bb_003B9C66[BB_003B9C66]
  bb_003B9C6C[BB_003B9C6C]
  bb_003B9C24 -->|branch| bb_003B9C66
  bb_003B9C24 -->|fallthrough| bb_003B9C45
  bb_003B9C45 -->|flow| bb_003B9C66
```
