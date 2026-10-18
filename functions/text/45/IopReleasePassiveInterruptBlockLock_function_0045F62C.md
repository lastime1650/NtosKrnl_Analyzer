# IopReleasePassiveInterruptBlockLock

- RVA: `0x0045F62C`–`0x0045F65D` (길이 `49` bytes)
- VA: `0x000000014045F62C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0045F639` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x0045F64D` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)

### Direct callers
- [IoProcessPassiveInterrupts](../39/IoProcessPassiveInterrupts_function_0039F85C.md) at `0x0039F8C6`
- [IopPassiveInterruptWorker](IopPassiveInterruptWorker_function_0045F3A0.md) at `0x0045F3F1`
- [IopPassiveInterruptWorker](IopPassiveInterruptWorker_function_0045F3A0.md) at `0x0045F43B`
- [IopDereferencePassiveInterruptBlock](IopDereferencePassiveInterruptBlock_function_0045F52C.md) at `0x0045F584`

### Static image references
- `0x0045F63E` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0045F62C  40 53                           push rbx
0045F62E  48 83 EC 20                     sub rsp, 0x20
0045F632  48 83 C1 38                     add rcx, 0x38
0045F636  0F B6 DA                        movzx ebx, dl
0045F639  E8 32 70 DA FF                  call 0x140206670
0045F63E  83 3D DB 76 B6 00 00            cmp dword ptr [rip + 0xb676db], 0
0045F645  74 0B                           je 0x14045f652
0045F647  44 0F 20 C1                     mov rcx, cr8
0045F64B  8A D3                           mov dl, bl
0045F64D  E8 46 60 09 00                  call 0x1404f5698
0045F652  44 0F 22 C3                     mov cr8, rbx
0045F656  48 83 C4 20                     add rsp, 0x20
0045F65A  5B                              pop rbx
0045F65B  C3                              ret
0045F65C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopReleasePassiveInterruptBlockLock(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (56);
    result = KxReleaseSpinLock(a1, a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 11957979)) != 0) {
        a1 = v_cr8;
        a2 = a2;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopReleasePassiveInterruptBlockLock(int64_t Arg1, uint8_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (56);
    result = KxReleaseSpinLock(Arg1, Arg2, a3, a4);
    if ((*(uint32_t *)(v_rip + 0xB676DB)) != 0) {
        Arg1 = v_cr8;
        Arg2 = Arg2;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0045F62C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0045F62C[BB_0045F62C]
  bb_0045F647[BB_0045F647]
  bb_0045F652[BB_0045F652]
  bb_0045F65C[BB_0045F65C]
  bb_0045F62C -->|branch| bb_0045F652
  bb_0045F62C -->|fallthrough| bb_0045F647
  bb_0045F647 -->|flow| bb_0045F652
```
