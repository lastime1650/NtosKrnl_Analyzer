# sub_0087F066

- RVA: `0x0087F066`–`0x0087F08B` (길이 `37` bytes)
- VA: `0x000000014087F066`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007C0F8`
- 디코드: `8`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0087F066  49 89 5B 18                     mov qword ptr [r11 + 0x18], rbx
0087F06A  33 D2                           xor edx, edx
0087F06C  49 89 6B E8                     mov qword ptr [r11 - 0x18], rbp
0087F070  65 48 8B 2C 25 88 01 00 00      mov rbp, qword ptr gs:[0x188]
0087F079  49 8B 80 78 02 00 00            mov rax, qword ptr [r8 + 0x278]
0087F080  49 89 73 E0                     mov qword ptr [r11 - 0x20], rsi
0087F084  40 B6 01                        mov sil, 1
0087F087  49 89 7B D8                     mov qword ptr [r11 - 0x28], rdi
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0087F066(__int64 a1, int a2, __int64 a3)
{
    *(unsigned __int64 *)(v_r11 + 24) = v_rbx;
    a2 = 0;
    *(unsigned __int64 *)(v_r11 - 24) = v_rbp;
    *(unsigned __int64 *)(v_r11 - 32) = v_rsi;
    *(unsigned __int64 *)(v_r11 - 40) = v_rdi;
    return *(unsigned __int64 *)(a3 + 632);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0087F066(int64_t Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    *(uint64_t *)(local_r11 + 0x18) = local_rbx;
    Arg2 = 0;
    *(uint64_t *)(local_r11 - 0x18) = local_rbp;
    *(uint64_t *)(local_r11 - 0x20) = local_rsi;
    *(uint64_t *)(local_r11 - 0x28) = local_rdi;
    return *(uint64_t *)(arg3 + 0x278);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x278` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0087F066&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0087F066[BB_0087F066]
```
