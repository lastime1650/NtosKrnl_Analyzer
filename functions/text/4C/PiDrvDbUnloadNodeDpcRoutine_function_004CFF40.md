# PiDrvDbUnloadNodeDpcRoutine

- RVA: `0x004CFF40`–`0x004CFFA4` (길이 `100` bytes)
- VA: `0x00000001404CFF40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `24`개 명령, `100/100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004CFF57` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x004CFF84` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x004CFF93` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x004CFF75` → RVA `0x00AAE570` (`PiDrvDbUnloadNodeWorkerCallback`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004CFF40  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004CFF45  57                              push rdi
004CFF46  48 83 EC 20                     sub rsp, 0x20
004CFF4A  48 8D BA A8 01 00 00            lea rdi, [rdx + 0x1a8]
004CFF51  48 8B DA                        mov rbx, rdx
004CFF54  48 8B CF                        mov rcx, rdi
004CFF57  E8 D4 84 D3 FF                  call 0x140208430
004CFF5C  80 BB B0 01 00 00 00            cmp byte ptr [rbx + 0x1b0], 0
004CFF63  75 2B                           jne 0x1404cff90
004CFF65  48 8D 8B 88 01 00 00            lea rcx, [rbx + 0x188]
004CFF6C  BA 01 00 00 00                  mov edx, 1
004CFF71  48 83 21 00                     and qword ptr [rcx], 0
004CFF75  48 8D 05 F4 E5 5D 00            lea rax, [rip + 0x5de5f4]
004CFF7C  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
004CFF80  48 89 59 18                     mov qword ptr [rcx + 0x18], rbx
004CFF84  E8 97 95 E2 FF                  call 0x1402f9520
004CFF89  C6 83 B0 01 00 00 01            mov byte ptr [rbx + 0x1b0], 1
004CFF90  48 8B CF                        mov rcx, rdi
004CFF93  E8 D8 66 D3 FF                  call 0x140206670
004CFF98  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004CFF9D  48 83 C4 20                     add rsp, 0x20
004CFFA1  5F                              pop rdi
004CFFA2  C3                              ret
004CFFA3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDrvDbUnloadNodeDpcRoutine(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = KeAcquireSpinLockAtDpcLevel(a2 + 424, a2, a3, a4);
    if ((*(unsigned __int8 *)(a2 + 432)) == 0) {
        a1 = a2 + 392;
        a2 = 1;
        result = v_rip + 6153716;
        *(unsigned __int64 *)(a1 + 16) = result;
        *(unsigned __int64 *)(a1 + 24) = a2;
        result = ExQueueWorkItem(a1, a2, a3, a4);
        *(unsigned __int8 *)(a2 + 432) = 1;
    }
    result = KxReleaseSpinLock(a2 + 424, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDrvDbUnloadNodeDpcRoutine(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = KeAcquireSpinLockAtDpcLevel(Arg2 + 424, Arg2, a3, a4);
    if ((*(uint8_t *)(arg2 + 0x1B0)) == 0) {
        Arg1 = Arg2 + 392;
        Arg2 = 1;
        result = v_rip + 6153716;
        *(uint64_t *)(Arg1 + 0x10) = result;
        *(void **)(Arg1 + 0x18) = Arg2;
        result = ExQueueWorkItem(Arg1, Arg2, a3, a4);
        *(uint8_t *)(arg2 + 0x1B0) = 1;
    }
    result = KxReleaseSpinLock(Arg2 + 424, Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R/W` |
| `Arg2` | `+ 0x10` | `64` | `W` |
| `Arg2` | `+ 0x18` | `64` | `W` |
| `Arg2` | `+ 0x188` | `64` | `R` |
| `Arg2` | `+ 0x1A8` | `64` | `R` |
| `Arg2` | `+ 0x1B0` | `8` | `R` |
| `Arg2` | `+ 0x1B0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004CFF40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004CFF40[BB_004CFF40]
  bb_004CFF65[BB_004CFF65]
  bb_004CFF90[BB_004CFF90]
  bb_004CFFA3[BB_004CFFA3]
  bb_004CFF40 -->|branch| bb_004CFF90
  bb_004CFF40 -->|fallthrough| bb_004CFF65
  bb_004CFF65 -->|flow| bb_004CFF90
```
