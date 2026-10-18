# KiVerifyXcpt12$fin$0

- RVA: `0x00C7FBAD`–`0x00C7FBCE` (길이 `33` bytes)
- VA: `0x0000000140C7FBAD`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BF6EC`
- 디코드: `14`개 명령, `33/33` bytes 표시
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
00C7FBAD  40 55                           push rbp
00C7FBAF  48 83 EC 20                     sub rsp, 0x20
00C7FBB3  48 8B EA                        mov rbp, rdx
00C7FBB6  84 C9                           test cl, cl
00C7FBB8  74 0D                           je 0x140c7fbc7
00C7FBBA  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
00C7FBBE  48 8B 02                        mov rax, qword ptr [rdx]
00C7FBC1  8B 08                           mov ecx, dword ptr [rax]
00C7FBC3  FF C1                           inc ecx
00C7FBC5  89 08                           mov dword ptr [rax], ecx
00C7FBC7  48 83 C4 20                     add rsp, 0x20
00C7FBCB  5D                              pop rbp
00C7FBCC  C3                              ret
00C7FBCD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiVerifyXcpt12_fin_0(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (a1 != 0) {
        a2 = *(unsigned __int64 *)(a2 + 64);
        result = *(unsigned __int64 *)(a2);
        a1 = *(unsigned int *)(result);
        a1 = (unsigned int)((a1) + 1);
        *(unsigned int *)(result) = a1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiVerifyXcpt12_fin_0(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (Arg1 != 0) {
        Arg2 = *(uint64_t *)(arg2 + 0x40);
        result = *(uint64_t *)(arg2);
        Arg1 = *(uint32_t *)(result);
        Arg1 = (uint32_t)((Arg1) + 1);
        *(uint32_t *)(result) = Arg1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C7FBAD&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C7FBAD[BB_00C7FBAD]
  bb_00C7FBBA[BB_00C7FBBA]
  bb_00C7FBC7[BB_00C7FBC7]
  bb_00C7FBCD[BB_00C7FBCD]
  bb_00C7FBAD -->|branch| bb_00C7FBC7
  bb_00C7FBAD -->|fallthrough| bb_00C7FBBA
  bb_00C7FBBA -->|flow| bb_00C7FBC7
```
