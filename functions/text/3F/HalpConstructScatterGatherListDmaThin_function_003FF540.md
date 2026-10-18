# HalpConstructScatterGatherListDmaThin

- RVA: `0x003FF540`–`0x003FF566` (길이 `38` bytes)
- VA: `0x00000001403FF540`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009A024`
- 디코드: `13`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalGetScatterGatherListDmaThin](HalGetScatterGatherListDmaThin_function_003FF370.md) at `0x003FF4FB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003FF540  48 8B C4                        mov rax, rsp
003FF543  48 89 48 08                     mov qword ptr [rax + 8], rcx
003FF547  53                              push rbx
003FF548  56                              push rsi
003FF549  41 54                           push r12
003FF54B  48 83 EC 50                     sub rsp, 0x50
003FF54F  48 8B 71 50                     mov rsi, qword ptr [rcx + 0x50]
003FF553  33 DB                           xor ebx, ebx
003FF555  44 8B 41 38                     mov r8d, dword ptr [rcx + 0x38]
003FF559  4C 8B D1                        mov r10, rcx
003FF55C  8B 51 3C                        mov edx, dword ptr [rcx + 0x3c]
003FF55F  44 8B DB                        mov r11d, ebx
003FF562  4C 8B 61 40                     mov r12, qword ptr [rcx + 0x40]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpConstructScatterGatherListDmaThin(__int64 a1)
{
    __int64 v_rbx;
    __int64 v_rsp;

    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (80);
    v_rbx = 0;
    return v_rsp;
}
```

## 5. (Beta) C Style

```c
int64_t HalpConstructScatterGatherListDmaThin(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rbx;
    int64_t local_rsp;

    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (80);
    local_rbx = 0;
    return local_rsp;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x3C` | `32` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FF540&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003FF540[BB_003FF540]
```
