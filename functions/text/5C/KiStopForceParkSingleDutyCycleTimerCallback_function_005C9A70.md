# KiStopForceParkSingleDutyCycleTimerCallback

- RVA: `0x005C9A70`–`0x005C9AE2` (길이 `114` bytes)
- VA: `0x00000001405C9A70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `29`개 명령, `114/114` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005C9A8D` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x005C9ABF` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x005C9AD1` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005C9A70  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005C9A75  57                              push rdi
005C9A76  48 83 EC 20                     sub rsp, 0x20
005C9A7A  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
005C9A80  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
005C9A85  48 8B DA                        mov rbx, rdx
005C9A88  33 D2                           xor edx, edx
005C9A8A  48 8B CB                        mov rcx, rbx
005C9A8D  E8 CE 52 D4 FF                  call 0x14030ed60
005C9A92  48 8B 9B F0 86 00 00            mov rbx, qword ptr [rbx + 0x86f0]
005C9A99  40 32 FF                        xor dil, dil
005C9A9C  83 BB 50 01 00 00 02            cmp dword ptr [rbx + 0x150], 2
005C9AA3  75 15                           jne 0x1405c9aba
005C9AA5  BF 01 00 00 00                  mov edi, 1
005C9AAA  C7 83 54 01 00 00 03 00 00 00   mov dword ptr [rbx + 0x154], 3
005C9AB4  89 BB 50 01 00 00               mov dword ptr [rbx + 0x150], edi
005C9ABA  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
005C9ABF  E8 8C 01 DD FF                  call 0x140399c50
005C9AC4  40 84 FF                        test dil, dil
005C9AC7  74 0D                           je 0x1405c9ad6
005C9AC9  45 33 C0                        xor r8d, r8d
005C9ACC  33 D2                           xor edx, edx
005C9ACE  48 8B CB                        mov rcx, rbx
005C9AD1  E8 7A E1 C3 FF                  call 0x140207c50
005C9AD6  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005C9ADB  48 83 C4 20                     add rsp, 0x20
005C9ADF  5F                              pop rdi
005C9AE0  C3                              ret
005C9AE1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiStopForceParkSingleDutyCycleTimerCallback(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(0, a2, v_stack_p10, a4);
    v_rdi = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 34544) + 336)) == 2) {
        v_rdi = 1;
        *(unsigned int *)(*(unsigned __int64 *)(a2 + 34544) + 340) = 3;
        *(unsigned int *)(*(unsigned __int64 *)(a2 + 34544) + 336) = (unsigned int)(v_rdi);
    }
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p10, a2, v_stack_p10, a4);
    if ((unsigned __int8)(v_rdi) != 0) {
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(a2 + 34544);
        result = KeInsertQueueDpc(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiStopForceParkSingleDutyCycleTimerCallback(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(0, Arg2, v_stack_p10, a4);
    local_rdi = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x86F0) + 0x150)) == 2) {
        local_rdi = 1;
        *(uint32_t *)(*(uint64_t *)(arg2 + 0x86F0) + 0x154) = 3;
        *(uint32_t *)(*(uint64_t *)(arg2 + 0x86F0) + 0x150) = (uint32_t)(local_rdi);
    }
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p10, Arg2, v_stack_p10, a4);
    if ((uint8_t)(local_rdi) != 0) {
        a3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg2 + 0x86F0);
        result = KeInsertQueueDpc(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x86F0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005C9A70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005C9A70[BB_005C9A70]
  bb_005C9AA5[BB_005C9AA5]
  bb_005C9ABA[BB_005C9ABA]
  bb_005C9AC9[BB_005C9AC9]
  bb_005C9AD6[BB_005C9AD6]
  bb_005C9AE1[BB_005C9AE1]
  bb_005C9A70 -->|branch| bb_005C9ABA
  bb_005C9A70 -->|fallthrough| bb_005C9AA5
  bb_005C9AA5 -->|flow| bb_005C9ABA
  bb_005C9ABA -->|branch| bb_005C9AD6
  bb_005C9ABA -->|fallthrough| bb_005C9AC9
  bb_005C9AC9 -->|flow| bb_005C9AD6
```
