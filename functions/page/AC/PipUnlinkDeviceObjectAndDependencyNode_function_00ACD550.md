# PipUnlinkDeviceObjectAndDependencyNode

- RVA: `0x00ACD550`–`0x00ACD598` (길이 `72` bytes)
- VA: `0x0000000140ACD550`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `20`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00ACD56E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00ACD587` → [PipDereferenceDependencyNode](PipDereferenceDependencyNode_function_00ACD5A0.md) (function, `0x00ACD5A0`)

### Direct callers
- [IoResolveDependency](../../text/4C/IoResolveDependency_function_004C4380.md) at `0x004C447D`
- [PipDeleteAllDependencyRelations](../A0/PipDeleteAllDependencyRelations_function_00A06950.md) at `0x00A06A0B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00ACD56E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ACD550  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00ACD555  57                              push rdi
00ACD556  48 83 EC 20                     sub rsp, 0x20
00ACD55A  48 8D 42 48                     lea rax, [rdx + 0x48]
00ACD55E  48 8B DA                        mov rbx, rdx
00ACD561  48 8B F9                        mov rdi, rcx
00ACD564  48 39 00                        cmp qword ptr [rax], rax
00ACD567  74 0A                           je 0x140acd573
00ACD569  BA 50 6E 70 44                  mov edx, 0x44706e50
00ACD56E  E8 6D A3 82 FF                  call 0x1402f78e0
00ACD573  48 8B 87 38 01 00 00            mov rax, qword ptr [rdi + 0x138]
00ACD57A  48 8B CB                        mov rcx, rbx
00ACD57D  48 83 60 50 00                  and qword ptr [rax + 0x50], 0
00ACD582  48 83 63 30 00                  and qword ptr [rbx + 0x30], 0
00ACD587  E8 14 00 00 00                  call 0x140acd5a0
00ACD58C  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00ACD591  48 83 C4 20                     add rsp, 0x20
00ACD595  5F                              pop rdi
00ACD596  C3                              ret
00ACD597  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipUnlinkDeviceObjectAndDependencyNode(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = a2 + 72;
    if ((*(unsigned __int64 *)(a2 + 72)) != (a2 + 72)) {
        a2 = 0x44706E50ULL;
        result = ObfDereferenceObjectWithTag(a1, a2, a3, a4);
    }
    result = PipDereferenceDependencyNode(a2, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipUnlinkDeviceObjectAndDependencyNode(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = Arg2 + 72;
    if ((*(uint64_t *)(arg2 + 0x48)) != (Arg2 + 72)) {
        Arg2 = 0x44706E50ULL;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, a3, a4);
    }
    result = PipDereferenceDependencyNode(Arg2, Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x138` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x30` | `64` | `R/W` |
| `Arg2` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ACD550&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ACD550[BB_00ACD550]
  bb_00ACD569[BB_00ACD569]
  bb_00ACD573[BB_00ACD573]
  bb_00ACD597[BB_00ACD597]
  bb_00ACD550 -->|branch| bb_00ACD573
  bb_00ACD550 -->|fallthrough| bb_00ACD569
  bb_00ACD569 -->|flow| bb_00ACD573
```
