# IopErrorLogDpc

- RVA: `0x005A3AA0`–`0x005A3AE5` (길이 `69` bytes)
- VA: `0x00000001405A3AA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `15`개 명령, `69/69` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x005A3AAB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x005A3ADA` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005A3AB0` → RVA `0x00F8D078` (`.data`; read/write)
- `0x005A3AB8` → RVA `0x00A5DC80` (`IopErrorLogThread`; read)
- `0x005A3ABF` → RVA `0x00F8D060` (`.data`; read/write)
- `0x005A3AC7` → RVA `0x00F8D060` (`.data`; read)
- `0x005A3AD3` → RVA `0x00F8D070` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x005A3AAB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005A3AA0  48 83 EC 28                     sub rsp, 0x28
005A3AA4  48 85 C9                        test rcx, rcx
005A3AA7  74 07                           je 0x1405a3ab0
005A3AA9  33 D2                           xor edx, edx
005A3AAB  E8 C0 ED 5D 00                  call 0x140b82870
005A3AB0  48 83 25 C0 95 9E 00 00         and qword ptr [rip + 0x9e95c0], 0
005A3AB8  48 8D 05 C1 A1 4B 00            lea rax, [rip + 0x4ba1c1]
005A3ABF  48 83 25 99 95 9E 00 00         and qword ptr [rip + 0x9e9599], 0
005A3AC7  48 8D 0D 92 95 9E 00            lea rcx, [rip + 0x9e9592]
005A3ACE  BA 01 00 00 00                  mov edx, 1
005A3AD3  48 89 05 96 95 9E 00            mov qword ptr [rip + 0x9e9596], rax
005A3ADA  E8 41 5A D5 FF                  call 0x1402f9520
005A3ADF  48 83 C4 28                     add rsp, 0x28
005A3AE3  C3                              ret
005A3AE4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopErrorLogDpc(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_rip + 10392982) = v_rip + 4956609;
    result = ExQueueWorkItem(v_rip + 10392978, 1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopErrorLogDpc(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    *(uint64_t *)(v_rip + 0x9E9596) = v_rip + 4956609;
    result = ExQueueWorkItem(v_rip + 10392978, 1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005A3AA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005A3AA0[BB_005A3AA0]
  bb_005A3AA9[BB_005A3AA9]
  bb_005A3AB0[BB_005A3AB0]
  bb_005A3AE4[BB_005A3AE4]
  bb_005A3AA0 -->|branch| bb_005A3AB0
  bb_005A3AA0 -->|fallthrough| bb_005A3AA9
  bb_005A3AA9 -->|flow| bb_005A3AB0
```
