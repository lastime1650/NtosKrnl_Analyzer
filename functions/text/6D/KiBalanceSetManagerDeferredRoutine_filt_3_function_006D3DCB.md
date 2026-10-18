# KiBalanceSetManagerDeferredRoutine$filt$3

- RVA: `0x006D3DCB`–`0x006D3DEF` (길이 `36` bytes)
- VA: `0x00000001406D3DCB`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B35E0`
- 디코드: `14`개 명령, `36/36` bytes 표시
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
006D3DCB  40 55                           push rbp
006D3DCD  48 83 EC 30                     sub rsp, 0x30
006D3DD1  48 8B EA                        mov rbp, rdx
006D3DD4  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D3DD7  83 C0 0A                        add eax, 0xa
006D3DDA  89 45 30                        mov dword ptr [rbp + 0x30], eax
006D3DDD  8B 4D 30                        mov ecx, dword ptr [rbp + 0x30]
006D3DE0  33 C0                           xor eax, eax
006D3DE2  83 F9 28                        cmp ecx, 0x28
006D3DE5  0F 94 C0                        sete al
006D3DE8  48 83 C4 30                     add rsp, 0x30
006D3DEC  5D                              pop rbp
006D3DED  C3                              ret
006D3DEE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiBalanceSetManagerDeferredRoutine_filt_3(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 48))) + (10));
    *(unsigned int *)(a2 + 48) = (unsigned int)(result);
    result = 0;
    result = (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48)))) == 40) ? 1 : 0;
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiBalanceSetManagerDeferredRoutine_filt_3(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x30))) + (10));
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)(result);
    result = 0;
    result = (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30)))) == 40) ? 1 : 0;
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x30` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D3DCB&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D3DCB[BB_006D3DCB]
  bb_006D3DEE[BB_006D3DEE]
```
